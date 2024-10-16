import tkinter as tk
from tkinter import messagebox


def close_app():
    root.quit()


def show_help():
    messagebox.showinfo("Acerca de", "Este es un mensaje informativo donde te estoy informando de alguna información.")


root = tk.Tk()
root.title("Ejercicio 9")
root.geometry("400x300")


# Barra de menú principal
main_menu = tk.Menu(root)
root.config(menu = main_menu)


# Menú Archivo
file_menu = tk.Menu(main_menu, tearoff = 0) # Se crea variable para la pestaña
main_menu.add_cascade(label = "Archivo", menu = file_menu) # Se hace un despegable en la pestaña
file_menu.add_command(label = "Abrir") # Se añade opción
file_menu.add_separator()
file_menu.add_command(label = "Salir", command = close_app) # Se añade opción con funcionalidad


# Menú Ayuda
help_menu = tk.Menu(main_menu, tearoff = 0)
main_menu.add_cascade(label = "Ayuda", menu = help_menu)
help_menu.add_command(label = "Acerca de", command = show_help)


root.mainloop()