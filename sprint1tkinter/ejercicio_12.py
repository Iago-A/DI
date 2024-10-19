import tkinter as tk
from tkinter import messagebox

from django.template.defaulttags import comment


def update_value(value):
    year_label.config(text = "Edad: " + value)


def show_option():
    option = radio_var.get()


def add_to_list():
    new_user = user_entry.get() + ", " + str(year_scale.get()) + ", " + radio_var.get()
    listbox.insert(tk.END, new_user)


def remove_from_list():
    # Obtener posiciones seleccionadas
    selected_users = listbox.curselection()

    # Eliminar usuarios de la lista
    # Usando reversed se invierten las posiciones para eliminar desde el final,
    # y así se evita que se desajusten los índices al eliminar elementos
    for index in reversed(selected_users):
        listbox.delete(index)


def close_window():
    root.quit()


def save_list():
    messagebox.showinfo("Aviso", "La lista se ha guardado correctamente")


def load_list():
    messagebox.showinfo("Aviso", "La lista se ha cargado")


root = tk.Tk()
root.title("Ejercicio 12")
root.geometry("350x540")


# Requisito 1: Entry
user_label = tk.Label(root, text = "Nombre de usuario:")
user_label.grid(row = 0, column = 0, padx = 5, pady = 10)

user_entry = tk.Entry(root, width = 30)
user_entry.grid(row = 0, column = 1, padx = 5, pady = 10)


# Requisito 2: Scale
year_label = tk.Label(root, text = "Edad: 0")
year_label.grid(row = 1, column = 0, padx = 5, pady = 10)

year_scale = tk.Scale(root, from_ = 0, to = 100, orient = "horizontal", command = update_value)
year_scale.grid(row = 1, column = 1, padx = 5, pady = 10)


# Requisito 3: Radiobutton
genre_label = tk.Label(root, text = "Género:")
genre_label.grid(row = 2, column = 0, padx = 5, pady = 10)

# Variable para Radiobutton
radio_var = tk.StringVar()
radio_var.set("Masculino") # Valor por defecto

genre_radiobutton1 = tk.Radiobutton(root, text = "Masculino", variable = radio_var, value = "Masculino", command = show_option)
genre_radiobutton1.grid(row = 2, column = 1, padx = 5, pady = 1, sticky = "w")

genre_radiobutton2 = tk.Radiobutton(root, text = "Femenino", variable = radio_var, value = "Femenino", command = show_option)
genre_radiobutton2.grid(row = 3, column = 1, padx = 5, pady = 1, sticky = "w")

genre_radiobutton3 = tk.Radiobutton(root, text = "Otro", variable = radio_var, value = "Otro", command = show_option)
genre_radiobutton3.grid(row = 4, column = 1, padx = 5, pady = 1, sticky = "w")


# Requisito 4: Botón añadir usuario
add_button = tk.Button(root, text = "Añadir usuario", command = add_to_list)
add_button.grid(row = 5, column = 1, padx = 5, pady = 10)


# Requisito 5: Listbox
# Frame para listbox y scrollbar
frame = tk.Frame(root, bg = "white", bd = 2, relief = "sunken")
frame.grid(row = 6, column = 1, padx = 10, pady = 10, columnspan = 2, sticky = "nsew")

# Lista usuarios
usuarios = ["Roberto, 27, Masculino",
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

listbox = tk.Listbox(frame, selectmode = tk.MULTIPLE, width = 30)
for usuario in usuarios:
    listbox.insert(tk.END, usuario)
listbox.grid(row = 0, column = 0, padx = 2, pady = 2)


# Requisito 6: Scrollbar
# Crear Scrollbar
scrollbar = tk.Scrollbar(frame, orient = "vertical", command = listbox.yview)
scrollbar.grid(row = 0, column = 1, sticky = "ns") # Para alinear a la derecha de la listbox

# Conectar listbox con scrollbar
listbox.config(yscrollcommand = scrollbar.set)


# Requisito 7: Botón eliminar usuario
remove_button = tk.Button(root, text = "Eliminar usuario", command = remove_from_list)
remove_button.grid(row = 8, column = 1, padx = 5, pady = 10)


# Requisito 8: Botón cerrar ventana
exit_button = tk.Button(root, text = "Salir", width = 10, command = close_window)
exit_button.grid(row = 9, column = 1, pady = 20, sticky = "se")


# Requisito 9: Menú
# Barra de menú
main_menu = tk.Menu(root)
root.config(menu = main_menu)

# Submenú
options_menu = tk.Menu(main_menu, tearoff = 0)
# Añadír submenú (de forma despegable) al menú principal
main_menu.add_cascade(label = "Opciones", menu = options_menu)
options_menu.add_command(label = "Guardar lista", command = save_list)
options_menu.add_separator()
options_menu.add_command(label = "Cargar lista", command = load_list)


root.mainloop()