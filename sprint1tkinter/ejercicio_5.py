import tkinter as tk

def change_colour():
    selection = var_radio.get()

    if(selection == "red"):
        root.config(bg = "red")
    if (selection == "green"):
        root.config(bg = "green")
    if (selection == "blue"):
        root.config(bg = "blue")


root = tk.Tk()
root.title("Ejercicio 5")
root.geometry("400x200")

# Crear variable para radiobuttons
var_radio = tk.StringVar()
var_radio.set("red") # Si no se establece una variable "inicial", todas las opciones aparecerían marcadas al abrir la ventana

label = tk.Label(root, text = "Seleccione su color favorito.")
label.pack(pady = 5)

# Crear radiobuttons como tal
radio1 = tk.Radiobutton(root, text = "Rojo", variable = var_radio, value = "red", command = change_colour)
radio1.pack()

radio2 = tk.Radiobutton(root, text = "Verde", variable = var_radio, value = "green", command = change_colour)
radio2.pack()

radio3 = tk.Radiobutton(root, text = "Azul", variable = var_radio, value = "blue", command = change_colour)
radio3.pack()

root.mainloop()
