import tkinter as tk

def show_text():
    # Obtener lo que se escriba en el entry
    name = entry.get()

    # También se puede concatenar un string con una variable name de la siguiente forma,
    # precedido de la f y con las {}
    label_2.config(text = f"Este es un saludo personalizado para {name}")


root = tk.Tk()
root.title("Ejercicio 3")
root.geometry("400x200")

label_1 = tk.Label(root, text = "Inserte su nombre:")
label_1.pack(pady = 10) # Márgen eje y

# Entry pedido en el ejercicio
entry = tk.Entry(root, width = 30)
entry.pack(pady = 5)

# Botón con la función de mostrar el siguiente label
button = tk.Button(root, text = "Mostrar saludo", command = show_text)
button.pack(pady = 10)

label_2 = tk.Label(root, text = "")
label_2.pack(pady = 10)

root.mainloop()