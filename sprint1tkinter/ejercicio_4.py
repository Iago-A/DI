import tkinter as tk

def show_selection():
    selection1 = var_check1.get()
    selection2 = var_check2.get()
    selection3 = var_check3.get()

    status = "Aficiones escogidas:" if selection1 or selection2 or selection3 else "Ninguna afición seleccionada."
    label2.config(text = status)

    # Crear una lista con las opciones escogidas.
    # El .append(elemento) añade ese elemento al final de la lista
    hobbies = []
    if selection1:
        hobbies.append("Leer")
    if selection2:
        hobbies.append("Deporte")
    if selection3:
        hobbies.append("Música")

    # Se actualiza el último label que al principio estaba vacio
    # El .join(lista) une el string indicado al elemento de la lista
    # si hay un True devuelto por haber aún algo en la lista
    label3.config(text = ", ".join(hobbies) if hobbies else "")


root = tk.Tk()
root.title("Ejercicio 4")
root.geometry("400x250")

# Variable para checkbutton
var_check1 = tk.IntVar()
var_check2 = tk.IntVar()
var_check3 = tk.IntVar()

label1 = tk.Label(root, text = "Seleccione sus aficiones.")
label1.pack(pady = 10)

# Crear el checkbutton leer como tal
checkbutton = tk.Checkbutton(root, text = "Leer", variable = var_check1, command = show_selection)
checkbutton.pack()

# Crear el checkbutton deporte como tal
checkbutton = tk.Checkbutton(root, text = "Deporte", variable = var_check2, command = show_selection)
checkbutton.pack()

# Crear el checkbutton música como tal
checkbutton = tk.Checkbutton(root, text = "Música", variable = var_check3, command = show_selection)
checkbutton.pack()

label2 = tk.Label(root, text = "Ninguna afición seleccionada.")
label2.pack(pady = 15)

label3 = tk.Label(root, text = "")
label3.pack()

root.mainloop()

