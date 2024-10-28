import tkinter as tk
from tkinter import messagebox


class Vista:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicio 1")
        self.root.geometry("")

        self.title_label = tk.Label(self.root, text="Aplicación de notas")
        self.title_label.pack(pady=10)

        self.coordinates_label = tk.Label(self.root, text="")
        self.coordinates_label.pack(pady=10)

        self.listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE)
        self.listbox.pack(pady=10)

        self.new_note_label = tk.Label(self.root, text="Insertar nueva nota:")
        self.new_note_label.pack()

        self.new_note_entry = tk.Entry(self.root, width=30)
        self.new_note_entry.pack(padx=80)

        self.add_button = tk.Button(self.root, text="Añadir nota")
        self.add_button.pack(pady=2)

        self.remove_button = tk.Button(self.root, text="Eliminar notas")
        self.remove_button.pack(pady=2)

        self.save_button = tk.Button(self.root, text="Guardar notas")
        self.save_button.pack(pady=2)

        self.load_button = tk.Button(self.root, text="Cargar notas")
        self.load_button.pack(pady=2)

        self.download_button = tk.Button(self.root, text="Descargar imagen")
        self.download_button.pack(pady=2)

        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady = 5)

        self.obtener_dimensiones_reales()
        self.centrar_ventana()


    def obtener_dimensiones_reales(self):
        self.root.update_idletasks()
        ancho = self.root.winfo_width()
        alto = self.root.winfo_height()
        self.root.geometry(f"{ancho}x{alto}")


    def centrar_ventana(self):
        self.root.update_idletasks()  # Asegura que las dimensiones sean correctas
        ancho = self.root.winfo_width()
        alto = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.root.winfo_screenheight() // 2) - (alto // 2)
        self.root.geometry(f"{ancho}x{alto}+{x}+{y}")


    def messagebox_note_saved(self):
        messagebox.showinfo("", "Las notas se han guardado correctamente")