import tkinter as tk
from ast import Bytes

from PIL import Image, ImageTk
import requests
from io import BytesIO
import threading


class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

        # Asociar eventos al widget principal
        self.vista.root.bind("<Button-1>", self.actualizar_coordenadas)

        # Añadir commands a los botones
        self.vista.add_button.config(command=self.agregar_nota)
        self.vista.remove_button.config(command=self.eliminar_nota)
        self.vista.save_button.config(command=self.guardar_notas)
        self.vista.load_button.config(command=self.cargar_notas)
        self.vista.download_button.config(command=self.descargar_imagen)


    def agregar_nota(self):
        nota = self.vista.new_note_entry.get()
        self.modelo.agregar_nota(nota)
        self.actualizar_listbox()


    def eliminar_nota(self):
        indice = self.vista.listbox.curselection()
        self.modelo.eliminar_nota(indice)
        self.actualizar_listbox()


    def guardar_notas(self):
        self.modelo.guardar_notas()
        self.vista.messagebox_note_saved()


    def cargar_notas(self):
        self.modelo.cargar_notas()
        self.actualizar_listbox()


    def descargar_imagen(self):
        url = "https://github.com/Iago-A/DI/blob/main/sprint2tkinter/resources/img/F-18.jpg?raw=true"
        hilo = threading.Thread(target=self.iniciar_descarga, args=(url, self.actualizar_etiqueta))
        hilo.start()


    def iniciar_descarga(self, url, callback):
        try:
            # Desacargar imagen
            descarga = requests.get(url)
            descarga.raise_for_status() # Lanza una excepción si la descarga falla.
            imagen = Image.open(BytesIO(descarga.content))
            imagen_redimensionada = imagen.resize((300, 200), Image.Resampling.LANCZOS)
            imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

            # Actualizar interfaz en hilo principal
            self.vista.root.after(0, callback, imagen_tk)
        except requests.exceptions.RequestException as e:
            self.vista.root.after(0, callback, None)


    def actualizar_etiqueta(self, imagen_tk):
        if imagen_tk:
            self.vista.image_label.config(image=imagen_tk)
            self.vista.image_label.image = imagen_tk  # Mantener una referencia

            # Ajustar la ventana después de configurar la imagen en el Label
            self.vista.root.update_idletasks()  # Asegura que los cambios en el Label se apliquen
            nuevo_ancho = self.vista.root.winfo_reqwidth()  # Ancho necesario para el contenido
            nuevo_alto = self.vista.root.winfo_reqheight()  # Alto necesario para el contenido
            self.vista.root.geometry(f"{nuevo_ancho}x{nuevo_alto}")

            self.vista.centrar_ventana()
        else:
            self.vista.image_label.config(text="Error al descargar la imagen.")


    def actualizar_coordenadas(self,event):
        x = event.x
        y = event.y

        # Verificar si el evento ocurrió en un botón
        widget_clicado = event.widget

        # Si el clic no ocurrió en un botón
        if not isinstance(widget_clicado, (tk.Button,)):
            self.vista.coordinates_label.config(text=f"Coordenadas: x= {x}, y= {y}")


    def actualizar_listbox(self):
        self.vista.listbox.delete(0, tk.END)
        notas = self.modelo.obtener_notas()

        for nota in notas:
            self.vista.listbox.insert(tk.END, nota)
