import tkinter as tk

class GameView:
    def __init__(self, on_card_click_callback, update_move_count_callback, update_time_callback):
        self.root = None
        self.labels = {}
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
        self.root.geometry("400x200")
        play_button = tk.Button(self.root, text="Jugar", command=start_game_callback)
        play_button.pack(pady=10)
        stats_button = tk.Button(self.root, text="Estadísticas", command=show_stats_callback)
        stats_button.pack(pady=10)
        exit_button = tk.Button(self.root, text="Salir", command=quit_callback)
        exit_button.pack(pady=10)


    def ask_player_name(self):
        pass


    def show_stats(self, stats):
        pass



