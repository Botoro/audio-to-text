'''main application for transcribing audio files to text using OpenAI's Whisper model'''
import datetime
import tempfile
import os
import streamlit as st
from openai import OpenAI

# Configuración
MAX_FILE_SIZE_MB = 30
allowed_audio_types = ["mp3", "mp4", "mpeg", "mpga", "m4a", "wav", "webm"]
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024
MAX_TEXT_LENGTH = 500  # Límite de caracteres para el texto transcrito


#Estilos
FOOTER="""<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    text-align: center;
}
</style>
<div class="footer">
<p>Made by <a href="https://github.com/Botoro/audio-to-text"> Botoro</a> with ❤️</p>
</div>
"""

TEXTAREA_STYLE="""<style>
textarea {
    resize: none !important;
}
</style>
"""

st.set_page_config(
    page_title="Texto a Audio - Botoro",
    page_icon="🤓",
    layout="centered"
)

st.title("Transcripción texto a audio")

api_key = st.text_input("Ingresa tu API Key", type="password")
if api_key:
    client = OpenAI(api_key=api_key)

    # Validar API key
    try:
        client.models.list()
    except Exception as e:
        st.error("❌ API key inválida. Verifícala e intenta de nuevo.")
        st.stop()

    language = st.selectbox("Idioma del audio", ["es", "en", "fr", "de"], help="Selecciona el \
        idioma para mejorar la transcripción")
    audio_file = st.file_uploader(
        "Sube tu archivo de audio", type=allowed_audio_types,
        help=f"Tipos de archivo permitidos: {', '.join(allowed_audio_types)}. \
            Tamaño máximo: {MAX_FILE_SIZE_MB} MB"
    )

    if audio_file:
        if audio_file.size > MAX_FILE_SIZE_BYTES:
            st.error(f"El archivo es demasiado grande. \
                El tamaño máximo permitido es {MAX_FILE_SIZE_MB} MB")
        else:
            original_filename = audio_file.name
            file_extension = os.path.splitext(original_filename)[1]

            with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as tmp_file:
                tmp_file.write(audio_file.read())
                temp_audio_path = tmp_file.name


            st.write("El Costo estimado de traducción es de **$0.006 USD** por minuto de audio.")
            st.caption("**Nota:** El modelo utilizado es Whisper-1. \
                Consulta la [página de precios](https://platform.openai.com/docs/pricing) \
                para obtener más información sobre los costos.")

            with open(temp_audio_path, "rb") as audio_file:
                try:
                    with st.spinner("Transcribiendo audio..."):
                        transcription = client.audio.transcriptions.create(
                            model="whisper-1",
                            file=audio_file,
                            language=language
                        )

                    st.success("✅ Transcripción Exitosa!")
                    st.subheader("Transcripción")
                    # Truncar texto si es muy largo
                    display_text = transcription.text[:MAX_TEXT_LENGTH]
                    if len(transcription.text) > MAX_TEXT_LENGTH:
                        display_text += "... (Texto completo disponible en la descarga)"
                    st.markdown(TEXTAREA_STYLE, unsafe_allow_html=True)
                    st.text_area("Texto transcrito", display_text, height=100)
                    st.download_button(
                        label="📥 Descargar .txt",
                        data=transcription.text,
                        file_name=f"transcription_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain",
                    )
                except Exception as e:
                    try:
                        error_message = e.args[0]
                        if "Incorrect API key" in error_message:
                            st.error("❌ API key inválida. Verifícala e intenta de nuevo.")
                        else:
                            st.error(f"❌ Error: {error_message}")
                    except Exception as inner_e:  # Catch a specific exception
                        st.error("❌ Un error inesperado ocurrió. \
                            Por favor intenta de nuevo más tarde.")
                finally:
                    os.remove(temp_audio_path)
st.markdown(FOOTER, unsafe_allow_html=True)