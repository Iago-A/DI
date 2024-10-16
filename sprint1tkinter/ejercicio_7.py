import tkinter as tk

def show_oval():
    x1, y1, x2, y2 = obtain_data()

    # Dibujar formas dentro del canvas
    canvas.create_oval(x1, y1, x2, y2, outline = "red")


def show_rectangle():
    x1, y1, x2, y2 = obtain_data()

    # Dibujar formas dentro del canvas
    canvas.create_rectangle(x1, y1, x2, y2, outline = "blue", width = 1)


def obtain_data():
    # Obtener datos de los entrys
    coordinates1 = entry1.get()
    coordinates2 = entry2.get()

    # Dividir el texto usando la coma como separador
    x1_str, y1_str = coordinates1.split(",")
    x2_str, y2_str = coordinates2.split(",")

    # Convertir String anteriiores a enteros
    x1 = int(x1_str)
    y1 = int(y1_str)
    x2 = int(x2_str)
    y2 = int(y2_str)

    return x1, y1, x2, y2


root = tk.Tk()
root.title("Ejercicio 7")
root.geometry("600x600")

label1 = tk.Label(root, text = "Coordenada esquina superior izquierda (x,y)")
label1.pack(pady = 10)

entry1 = tk.Entry(root, width = 30)
entry1.pack()

# Genero una etiqueta invisible para crear una pequeña separación en la ventana
invisible_label = tk.Label(root, text = "")
invisible_label.pack(pady = 3)

label2 = tk.Label(root, text = "Coordenada esquina inferior derecha (x,y)")
label2.pack(pady = 10)

entry2 = tk.Entry(root, width = 30)
entry2.pack()

# Genero una etiqueta invisible para crear una pequeña separación en la ventana
invisible_label = tk.Label(root, text = "")
invisible_label.pack(pady = 3)

button_oval = tk.Button(root, text = "Generar óvalo", command = show_oval)
button_oval.pack(pady = 5)

button_rentangle = tk.Button(root, text = "Generar rectángulo", command = show_rectangle)
button_rentangle.pack(pady = 5)

# Crear el canvas
canvas = tk.Canvas(root, width = 400, height = 300, bg = "white")
canvas.pack(pady = 20)

root.mainloop()