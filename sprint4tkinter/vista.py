import tkinter as tk

class GameView:
    def __init__(self, on_card_click_callback, update_move_count_callback, update_time_callback):
        # self.labels?? no entiendo
        self.on_card_click_callback = on_card_click_callback
        self.update_move_count_callback = update_move_count_callback
        self.update_time_callback = update_time_callback


    def create_board(self, model):
        pass


    def update_board(self, pos, image_id):
        pass


    def reset_cards(self, pos1, pos2):
        pass


    def update_move(self, moves):
        pass


    def update_time(self, time):
        pass


    def destroy(self):
        pass


class MainMenu:
    def __init__(self, root, start_game_callback, show_stats_callback, quit_callback):
        self.root = root
        self.root.title("Juego de memoria")
        self.root.geometry("400x600")

        # Barra de menú principal
        main_menu = tk.Menu(root)
        root.config(menu=main_menu)

        # Casilla opciones
        options_menu = tk.Menu(main_menu, tearoff=0) # Variable para la casilla
        main_menu.add_cascade(label="Opciones", menu=options_menu)
        options_menu.add_command(label="Jugar", command="")
        options_menu.add_separator()
        options_menu.add_command(label="Estadísticas", command="")
        options_menu.add_separator()
        options_menu.add_command(label="Salir", command="")


    def ask_player_name(self):
        pass


    def show_stats(self, stats):
        pass



