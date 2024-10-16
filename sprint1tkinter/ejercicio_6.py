import tkinter as tk


def show_fruits():
    # .curseselection devuelve los índices de los elementos seleccionados
    selection = listbox.curselection()

    # Convertir los índices a los nombres de las frutas
    fruits_selected = [listbox.get(i) for i in selection]

    # Mostrar el resultado en la etiqueta
    label.config(text=", ".join(fruits_selected))


root = tk.Tk()
root.title = "Ejercicio 6"
root.geometry("400x300")

# Se crea la lista de opciones para la listbox
options = ["Manzana", "Pera", "Plátano", "Fresa", "Cereza", "Melocotón"]

# Crear listbox
listbox = tk.Listbox(root, selectmode = tk.MULTIPLE)
for selected in options:
    listbox.insert(tk.END, selected)
listbox.pack(pady = 10)

button = tk.Button(root, text = "Mostrar frutas seleccionadas", command = show_fruits)
button.pack(pady = 5)

label = tk.Label(root, text = "")
label.pack(pady = 10)

root.mainloop()