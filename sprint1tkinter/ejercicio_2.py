import tkinter as tk

def show_text():
    label.config(text = "Ahora me ves")


def close_window():
    root.quit()


# Crear ventana
root = tk.Tk()
root.title = "Ejercicio 2"
root.geometry("400x250")

# Primer botón
button1 = tk.Button(root, text = "Clic para mostrar texto", command = show_text)
button1.pack()

label = tk.Label(root, text = "")
label.pack(pady = 10) # Márgen eje y

# Segundo botón
button2 = tk.Button(root, text = "Cerrar ventana", command = close_window)
button2.pack()

root.mainloop()