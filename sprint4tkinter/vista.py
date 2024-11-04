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
        pass


    def ask_player_name(self):
        pass


    def show_stats(self, stats):
        pass



