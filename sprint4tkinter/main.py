import tkinter as tk
from controlador import GameController
from modelo import GameModel
from vista import MainMenu
from vista import GameView


def main():
    root = tk.Tk()
    model = GameModel()
    main_menu = MainMenu(root)
    game_view = GameView(root)
    controller = GameController(model, main_menu, game_view)

    root.mainloop()


if __name__ == "__main__":
    main()


