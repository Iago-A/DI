import tkinter as tk

def cambiar_texto():
    etiqueta_3.config(text = "pero ahora digo lo otro.")

# Creación de ventana
root = tk.Tk()
root.title("Ejercicio 1")
root.geometry("400x250")

# Primera etiqueta Label
etiqueta_1 = tk.Label(root, text = "Bienvenido a mi ventana.")
etiqueta_1.pack()

# Segunda etiqueta
etiqueta_2 = tk.Label(root, text = "Soy Iago Blanco.")
etiqueta_2.pack()

# Tercera etiqueta
etiqueta_3 = tk.Label(root, text = "Ahora digo esto...")
etiqueta_3.pack()

# Botón
boton = tk.Button(root, text = "Clic para cambiar texto de arriba", command = cambiar_texto)
boton.pack()


root.mainloop()



# Crea una ventana que muestre tres etiquetas (Label). La primera
# debe mostrar un mensaje de bienvenida, la segunda debe mostrar tu
# nombre, y la tercera debe cambiar su texto al hacer clic en un botón.