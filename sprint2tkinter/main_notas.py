import tkinter as tk
from modelo import Modelo
from vista import Vista
from controlador import Controlador

def main():
    root = tk.Tk()
    modelo = Modelo()
    vista = Vista(root)
    controlador = Controlador(modelo, vista)

    root.mainloop()


if __name__ == "__main__":
    main()