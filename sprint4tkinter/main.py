import tkinter as tk
from controlador import GameController
from modelo import GameModel
from vista import MainMenu, GameView

def main():
    root = tk.Tk()
    model = GameModel("fácil", "")
    main_menu = MainMenu(root)  # Instanciamos sin pasar callbacks
    game_view = GameView(None, None, None)  # Estos callbacks los configurará el controlador
    controller = GameController(root, model, main_menu, game_view)

    root.mainloop()

if __name__ == "__main__":
    main()

