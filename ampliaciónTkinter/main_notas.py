import tkinter as tk
from modelo_notas import Modelo
from vista_notas import Vista
from controlador_notas import Controlador

def main():
    root = tk.Tk()
    modelo = Modelo()
    vista = Vista(root)
    controlador = Controlador(modelo, vista)

    root.mainloop()


if __name__ == "__main__":
    main()