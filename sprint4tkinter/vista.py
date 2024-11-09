import tkinter as tk
from tkinter import simpledialog


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
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de memoria")
        self.root.geometry("400x200")

        # Creamos los botones sin asignar sus comandos
        self.play_button = tk.Button(self.root, text="Jugar")
        self.play_button.pack(pady=10)

        self.stats_button = tk.Button(self.root, text="Estadísticas")
        self.stats_button.pack(pady=10)

        self.exit_button = tk.Button(self.root, text="Salir")
        self.exit_button.pack(pady=10)

    def set_callbacks(self, start_game_callback, show_stats_callback, quit_callback):
        # Asignamos los callbacks a cada botón
        self.play_button.config(command=start_game_callback)
        self.stats_button.config(command=show_stats_callback)
        self.exit_button.config(command=quit_callback)

    def ask_player_name(self):
        player_name = simpledialog.askstring("Nombre jugador", "Inserte nombre:", parent=self.root)
        print(f"Nombre del jugador: {player_name}")
        return player_name

    def show_stats(self, stats):
        pass
