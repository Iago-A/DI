import tkinter as tk

def update_value(value):
    label.config(text = "Valor: " + value)


root = tk.Tk()
root.title("Ejercicio 11")
root.geometry("400x200")


# Creación scale
scale = tk.Scale(root, from_ = 0, to = 100, orient = "horizontal", command = update_value)
scale.pack(pady = 20)


# Label para mostrar valor
label = tk.Label(root, text = "Valor: 0")
label.pack(pady = 10)


root.mainloop()