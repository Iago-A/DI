import tkinter as tk
import time
from tkinter import simpledialog


class GameController:
    def __init__(self, root, model, main_menu, game_view):
        self.root = root
        self.model = model
        self.main_menu = main_menu
        self.game_view = game_view

        # Enlazamos los callbacks del controlador al menú principal
        self.main_menu.set_callbacks(self.start_game, self.show_stats, self.quit_game)


    def show_difficulty_selection(self):
        difficulty = simpledialog.askstring("Seleccione la dificultad","Ingrese la dificultad (fácil, medio, difícil):", parent=self.root)
        if len(difficulty) > 0:
            if difficulty == "fácil" or difficulty == "medio" or difficulty == "difícil":
                # Se cambian los atributos dificultad y nombre 'hardcodeados' en el main
                self.model.difficulty = difficulty
                self.model.player_name = self.main_menu.ask_player_name()
                print(f"Dificultad {self.model.difficulty} nombre {self.model.player_name}")
            else:
                print("Dificultad no válida")
        else:
            print("No se seleccionó ninguna dificultad")


    def start_game(self):
        difficulty = self.model.difficulty

        self.show_difficulty_selection()


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
        print("Aquí saldrían unas estadísticas de la leche")


    def update_time(self):
        pass


    def quit_game(self):
        self.root.quit()

    
