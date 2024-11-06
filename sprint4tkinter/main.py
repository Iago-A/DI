import tkinter as tk
from controlador import GameController
from modelo import GameModel
from vista import MainMenu
from vista import GameView


def main():
    root = tk.Tk()
    model = GameModel("Easy", "Iago")
    main_menu = MainMenu(root, start_game_callback, show_stats_callback, quit_callback)
    game_view = GameView(on_card_click_callback, update_move_count_callback, update_time_callback)
    controller = GameController(model)

    root.mainloop()


if __name__ == "__main__":
    main()


