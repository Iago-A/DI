import tkinter as tk
from tkinter import messagebox


class SimpleAppManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicio 12")
        self.root.geometry("350x540")

        # Requisito 1: Entry
        self.user_label = tk.Label(self.root, text="Nombre de usuario:")
        self.user_label.grid(row=0, column=0, padx=5, pady=10)

        self.user_entry = tk.Entry(self.root, width=30)
        self.user_entry.grid(row=0, column=1, padx=5, pady=10)

        # Requisito 2: Scale
        self.year_label = tk.Label(self.root, text="Edad: 0")
        self.year_label.grid(row=1, column=0, padx=5, pady=10)

        self.year_scale = tk.Scale(self.root, from_=0, to=100, orient="horizontal", command=self.update_value)
        self.year_scale.grid(row=1, column=1, padx=5, pady=10)

        # Requisito 3: Radiobutton
        self.genre_label = tk.Label(self.root, text="Género:")
        self.genre_label.grid(row=2, column=0, padx=5, pady=10)

        # Variable para Radiobutton
        self.radio_var = tk.StringVar()
        self.radio_var.set("Masculino")  # Valor por defecto

        self.genre_radiobutton1 = tk.Radiobutton(self.root, text="Masculino", variable=self.radio_var, value="Masculino",
                                            command=self.show_option)
        self.genre_radiobutton1.grid(row=2, column=1, padx=5, pady=1, sticky="w")

        self.genre_radiobutton2 = tk.Radiobutton(self.root, text="Femenino", variable=self.radio_var, value="Femenino",
                                            command=self.show_option)
        self.genre_radiobutton2.grid(row=3, column=1, padx=5, pady=1, sticky="w")

        self.genre_radiobutton3 = tk.Radiobutton(self.root, text="Otro", variable=self.radio_var, value="Otro", command=self.show_option)
        self.genre_radiobutton3.grid(row=4, column=1, padx=5, pady=1, sticky="w")

        # Requisito 4: Botón añadir usuario
        self.add_button = tk.Button(self.root, text="Añadir usuario", command=self.add_to_list)
        self.add_button.grid(row=5, column=1, padx=5, pady=10)

        # Requisito 5: Listbox
        # Frame para listbox y scrollbar
        self.frame = tk.Frame(self.root, bg="white", bd=2, relief="sunken")
        self.frame.grid(row=6, column=1, padx=10, pady=10, columnspan=2, sticky="nsew")

        # Lista usuarios
        self.usuarios = ["Roberto, 27, Masculino",
                         "Marta, 18, Femenino",
                         "Victoria, 58, Femenino",
                         "Víctor, 12, Masculino",
                         "Enrique, 43, Masculino",
                         "Laura, 24, Otro",
                         "Martín, 29, Masculino",
                         "Fernando, 33, Masculino",
                         "Julián, 21, Masculino",
                         "Uxia, 8, Femenino",
                         "Claudia, 41, Femenino",
                         "Gabriela, 18, Femenino",
                         "Javier, 37, Masculino",
                         "Pablo, 40, Masculino",
                         "Ana, 24, Femenino",
                         "Berto, 34, Masculino",
                         "Juliet, 26, Otro",
                         "Marcos, 46, Masculino",
                         "Sara, 14, Femenino",
                         "Emilio, 64, Masculino",
                         "María, 72, Femenino",
                         "Dolores, 78, Femenino",
                         "Joel, 16, Masculino"]

        self.listbox = tk.Listbox(self.frame, selectmode=tk.MULTIPLE, width=30)
        for usuario in self.usuarios:
            self.listbox.insert(tk.END, usuario)
        self.listbox.grid(row=0, column=0, padx=2, pady=2)

        # Requisito 6: Scrollbar
        # Crear Scrollbar
        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.listbox.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")  # Para alinear a la derecha de la listbox

        # Conectar listbox con scrollbar
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        # Requisito 7: Botón eliminar usuario
        self.remove_button = tk.Button(self.root, text="Eliminar usuario", command=self.remove_from_list)
        self. remove_button.grid(row=8, column=1, padx=5, pady=10)

        # Requisito 8: Botón cerrar ventana
        self.exit_button = tk.Button(self.root, text="Salir", width=10, command=self.close_window)
        self.exit_button.grid(row=9, column=1, pady=20, sticky="se")

        # Requisito 9: Menú
        # Barra de menú
        self.main_menu = tk.Menu(self.root)
        self.root.config(menu=self.main_menu)

        # Submenú
        self.options_menu = tk.Menu(self.main_menu, tearoff=0)
        # Añadír submenú (de forma despegable) al menú principal
        self.main_menu.add_cascade(label="Opciones", menu=self.options_menu)
        self.options_menu.add_command(label="Guardar lista", command=self.save_list)
        self.options_menu.add_separator()
        self.options_menu.add_command(label="Cargar lista", command=self.load_list)


    def update_value(self, value):
        self.year_label.config(text = "Edad: " + value)


    def show_option(self):
        option = self.radio_var.get()


    def add_to_list(self):
        new_user = self.user_entry.get() + ", " + str(self.year_scale.get()) + ", " + self.radio_var.get()
        self.listbox.insert(tk.END, new_user)


    def remove_from_list(self):
        # Obtener posiciones seleccionadas
        selected_users = self.listbox.curselection()

        # Eliminar usuarios de la lista
        # Usando reversed se invierten las posiciones para eliminar desde el final,
        # y así se evita que se desajusten los índices al eliminar elementos
        for index in reversed(selected_users):
            self.listbox.delete(index)


    def close_window(self):
        root.quit()


    def save_list(self):
        messagebox.showinfo("Aviso", "La lista se ha guardado correctamente")


    def load_list(self):
        messagebox.showinfo("Aviso", "La lista se ha cargado")


if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleAppManagement(root)
    root.mainloop()