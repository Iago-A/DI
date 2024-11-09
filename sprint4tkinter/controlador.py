import tkinter as tk
import time

class GameController:
    def __init__(self, root, model, main_menu, game_view):
        self.root = root
        self.model = model
        self.main_menu = main_menu
        self.game_view = game_view

        # Enlazar los botones del menú principal de vista con los métodos de este fichero
        self.main_menu.start_game_callback = self.start_game
        self.main_menu.show_stats_callback = self.show_stats
        self.main_menu.quit_callback = self.quit_game


    def show_difficulty_selection(self):
        pass


    def start_game(self, difficulty):
        print("Juego iniciado")


    def show_loading_window(self, message):
        pass


    def check_images_loades(self):
        pass


    def on_card_click(self, pos):
        pass


    def handle_card_selection(self):
        pass


    def update_move_count(self, moves):
        pass


    def check_game_complete(self):
        pass


    def return_to_main_menu(self):
        pass


    def show_stats(self):
        pass


    def update_time(self):
        pass


    def quit_game(self):
        quit()

    
