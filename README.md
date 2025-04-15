# Aplicación de Audio a Texto

Esta aplicación transcribe archivos de audio a texto utilizando el modelo Whisper de OpenAI. Fue creada para facilitar el uso de la API de OpenAI y transformar audio a texto de manera sencilla.

## Requisitos

*   Python 3.7+
*   pip
*   Una clave de API de OpenAI

## Configuración

1.  **Clona el repositorio:**

    ```bash
    git clone https://github.com/Botoro/audio-to-text.git
    cd audio-a-texto
    ```


2.  **Crea un entorno virtual (recomendado):**

    ```bash
    python3 -m venv venv
    ```

3.  **Activa el entorno virtual:**

    *   En macOS y Linux:

        ```bash
        source venv/bin/activate
        ```

    *   En Windows:

        ```bash
        .\venv\Scripts\activate
        ```

4.  **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuración Adicional

1.  **Obtén una clave de API de OpenAI:**

    *   Regístrate en [https://platform.openai.com/](https://platform.openai.com/).
    *   Crea una nueva clave de API en [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys).

2.  **Establece la clave de API de OpenAI:**

    *   La aplicación te pedirá que ingreses tu clave de API cuando la ejecutes.

## Ejecutando la Aplicación

1.  **Ejecuta la aplicación Streamlit:**

    ```bash
    streamlit run app.py
    ```

2.  **Abre la aplicación en tu navegador:**

    *   Streamlit proporcionará una URL en la terminal (generalmente `http://localhost:8501`). Abre esta URL en tu navegador web.

## Uso

1.  Ingresa tu clave de API de OpenAI en el campo de texto proporcionado.
2.  Selecciona el idioma del audio.
3.  Sube un archivo de audio (mp3, wav, m4a, etc.).
4.  La aplicación transcribirá el audio y mostrará el texto.
5.  Puedes descargar la transcripción como un archivo `.txt`.

## Notas

*   La aplicación utiliza el modelo Whisper-1 para la transcripción.
*   La estimación de costos es aproximada y puede variar.
*   El tamaño máximo del archivo es de 30MB.

## Contribución

Siéntete libre de contribuir a este proyecto enviando pull requests.


## Licencia

Este proyecto no tiene una licencia específica. Puedes usarlo, modificarlo y distribuirlo libremente, pero se agradece dar crédito al autor original.

Este proyecto fue creado utilizando [Streamlit](https://streamlit.io/).