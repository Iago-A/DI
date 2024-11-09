import tkinter as tk
from controlador import GameController
from modelo import GameModel
from vista import MainMenu
from vista import GameView


def main(start_game_callback=None, show_stats_callback=None, quit_callback=None, on_card_click_callback=None,
         update_move_count_callback=None, update_time_callback=None):
    root = tk.Tk()
    model = GameModel("Easy", "Iago")
    main_menu = MainMenu(root, start_game_callback, show_stats_callback, quit_callback)
    game_view = GameView(on_card_click_callback, update_move_count_callback, update_time_callback)
    controller = GameController(root, model, main_menu, game_view)

    root.mainloop()


if __name__ == "__main__":
    main()


