import threading
import time
import random
import datetime

from recursos import descargar_imagen

class GameModel:
    def __init__(self, difficulty, player_name, cell_size=100):
        self.difficulty = difficulty
        self.player_name = player_name
        self.cell_size = cell_size

        # Incompleto


    def _generate_board(self):
        pass


    def _load_images(self):
        pass


    def images_are_loaded(self):
        pass


    def start_timer(self):
        pass


    def get_time(self):
        pass


    def check_match(self, pos1, pos2):
        pass


    def is_game_complete(self):
        pass


    def load_scores(self):
        pass
