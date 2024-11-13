import threading

import requests
from PIL import Image, ImageTk
from io import BytesIO


def descargar_imagen(url, size):
    try:
        response = requests.get(url)
        response.raise_for_status() # Lanza una excepción si la descarga falla
        imagen = Image.open(BytesIO(response.content))
        imagen_redimensionada = imagen.resize(size, Image.Resampling.LANCZOS)
        imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

        print(f"Imagen con url {url} descargada.")
        return imagen_tk
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la imagen desde {url}: {e}")
        return None
