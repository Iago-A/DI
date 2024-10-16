import tkinter as tk

def show_phrase():
    phrase = entry.get()

    label2.config(text = phrase)


def delete_phrase():
    label2.config(text = "")
    entry.delete(0, tk.END)

# Ventana principal
root = tk.Tk()
root.title("Ejercicio 8")
root.geometry("400x400")


# Crear frame superior
frame_sup = tk.Frame(root, bg = "lightgrey", bd = 2, relief = "sunken")
frame_sup.pack(padx = 20, pady = 20, fill = 'both', expand = True)


# Insertar widgets frame superior
label1 = tk.Label(frame_sup, text = "Escribe tu frase favorita:", bg = "lightgrey")
label1.pack(pady = 20)

entry = tk.Entry(frame_sup, width = 30)
entry.pack(pady = 5)

label2 = tk.Label(frame_sup, text = "", bg = "lightgrey")
label2.pack(pady = 30)


# Crear frame inferior
frame_inf = tk.Frame(root, bg = "lightgrey", bd = 2, relief = "sunken")
frame_inf.pack(padx = 20, pady = 20, fill = 'both', expand = True)

# Insertar widgets frame inferior
button1 = tk.Button(frame_inf, text = "Mostrar frase", command = show_phrase)
button1.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'ew')

button2 = tk.Button(frame_inf, text = "Borrar frase", command = delete_phrase)
button2.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = 'ew')


root.mainloop()