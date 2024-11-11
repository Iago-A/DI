import threading

import requests
from PIL import Image, ImageTk
from io import BytesIO


def descargar_imagen(url, size, callback=None):
    load_images_thread = threading.Thread(target=iniciar_descarga, args=(url, (size,size-100), callback))
    load_images_thread.start()

    return load_images_thread

def iniciar_descarga(url, size, callback):
    try:
        response = requests.get(url)
        response.raise_for_status() # Lanza una excepción si la descarga falla
        imagen = Image.open(BytesIO(response.content))
        imagen_redimensionada = imagen.resize(size, Image.Resampling.LANCZOS)
        imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

        # Llamamos al callback si está definido
        if callback:
            callback(imagen_tk)  # Llama al callback cuando la imagen se ha descargado

        return imagen_tk
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la imagen desde {url}: {e}")
        return None
