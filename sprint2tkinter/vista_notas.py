import tkinter as tk

class Vista:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicio 1")
        self.root.geometry("400x300")

        title_label = tk.Label(self.root, text="Aplicación de notas")
        title_label.pack(pady=10)

        coordinates_label = tk.Label(self.root, text="")
        coordinates_label.pack(pady=10)

        # Lista de notas para la listbox
        list = ["Primera nota de prueba",
                 "Comprar leche",
                 "Buscar tesoro",
                 "Felicitar a Joel"]

        listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE)
        # Añadir notas a la lista
        for note in list:
            listbox.insert(tk.END, note)
        listbox.pack(pady=10)

        new_note_label = tk.Label(self.root, text="Insertar nueva nota:")
        new_note_label.pack()

        new_note_entry = tk.Entry(self.root, width=30)
        new_note_entry.pack()

        add_button = tk.Button(self.root, text="Añadir nota")
        add_button.pack(pady=2)

        remove_button = tk.Button(self.root, text="Eliminar notas")
        remove_button.pack(pady=2)

        save_button = tk.Button(self.root, text="Guardar notas")
        save_button.pack(pady=2)

        remove_button = tk.Button(self.root, text="Eliminar notas")
        remove_button.pack(pady=2)

