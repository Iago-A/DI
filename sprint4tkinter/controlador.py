import tkinter as tk
from tkinter import simpledialog


class GameController:
    def __init__(self, root, model, main_menu, game_view):
        self.root = root
        self.model = model
        self.main_menu = main_menu
        self.game_view = game_view
        self.loading_window = None # Esta variable es para almacenar la ventana de carga y poder destruirla después.
        self.selected = [] # Variable para almacenar la posición de las carta clicadas
        self.moves = 0

        # Enlazamos los callbacks del controlador al menú principal
        self.main_menu.set_callbacks(self.start_game, self.show_stats, self.quit_game)

        # Enlazamos los callbacks del controlador al game view
        self.game_view.set_callbacks(self.on_card_click, self.update_move_count, self.update_time)

    def show_difficulty_selection(self):
        difficulty = simpledialog.askstring("Seleccione la dificultad","Ingrese la dificultad (fácil, medio, difícil):", parent=self.root)
        if len(difficulty) > 0:
            if difficulty == "fácil" or difficulty == "medio" or difficulty == "difícil":
                # Se cambian los atributos dificultad y nombre 'hardcodeados' en el main
                self.model.difficulty = difficulty
                self.model.player_name = self.main_menu.ask_player_name()
                print(f"Dificultad {self.model.difficulty} nombre {self.model.player_name}")

                return True
            else:
                print("Dificultad no válida")
                return False
        else:
            print("No se seleccionó ninguna dificultad")
            return False


    def start_game(self):
        difficulty = self.model.difficulty
        ready_to_start = False # Si se escoge mal la dificultad, seguirá en false

        ready_to_start = self.show_difficulty_selection()
        if ready_to_start:
            self.model._generate_board()
            self.show_loading_window("Cargando...")

            self.model._load_images()
            self.check_images_loaded() # Se destruye la ventana de carga

            # Usa after para cargar las imágenes de forma asíncrona y eliminar la ventana de carga cuando estén listas.
            # self.root.after(1000, self.model._load_images)  # Llama a _load_images después de 1000 ms.
            # self.root.after(2000, self.check_images_loaded)  # Comprueba si las imágenes se cargaron y cierra la ventana de carga.

        else:
            print("El juego no se pudo iniciar.")


    def show_loading_window(self, message):
        self.loading_window = tk.Toplevel(self.root)
        self.loading_window.title("")
        self.loading_window.geometry("200x200")
        label = tk.Label(self.loading_window, text=message)
        label.pack()

        self.loading_window.update()  # Actualiza para que se muestre de inmediato


    def check_images_loaded(self):
        print("Todas las imágenes descargadas.")
        self.loading_window.destroy()
        self.game_view.create_board(self.model)  # Crea el tablero


    def on_card_click(self, event, position):
        print(f"Carta seleccionada en posición: {position}")

        # Evitar seleccionar la misma carta dos veces
        if position in self.selected:
            return

        # Actualizar contador movimientos
        self.update_move_count()

        # Guardar posición de la carta el self.selected
        self.selected.append(position)

        # Mostramos la imagen de la carta seleccionada temporalmente
        carta = self.model.board[position[0]][position[1]]
        self.game_view.update_board(position, self.model.images[carta])

        # Si hay dos cartas seleccionadas, comprobamos si hay coincidencia
        if len(self.selected) == 2:
            self.handle_card_selection()

        if not self.model.timer_running:
            self.model.start_timer()

        # Actualiza el tiempo
        self.update_time()
        self.root.after(1000, self.update_time_continuously)  # Luego continuar actualizando cada 1000 ms


    def update_time_continuously(self):
        self.update_time()  # Llama a la función de actualización del label del tiempo

        # Después de 1000 ms, vuelve a llamar a esta misma función para seguir actualizando el tiempo
        self.root.after(1000, self.update_time_continuously)


    def handle_card_selection(self):
        # Extraer las posiciones seleccionadas
        pos1, pos2 = self.selected

        # Obtener las cartas en las posiciones seleccionadas
        carta1 = self.model.board[pos1[0]][pos1[1]]
        carta2 = self.model.board[pos2[0]][pos2[1]]

        # Comprobamos si las cartas coinciden
        if carta1 == carta2:
            # Las cartas coinciden, las dejamos descubiertas
            print("¡Coincidencia!")
            self.selected = []  # Reiniciamos las seleccionadas
        else:
            # Las cartas no coinciden, las ocultamos después de un breve retraso
            self.game_view.ventana.after(1000, lambda: self.game_view.reset_cards(pos1, pos2))
            self.selected = []  # Reiniciamos las seleccionadas


    def update_move_count(self):
        self.moves += 1
        print(f"Movimientos actualizados: {self.moves}")
        self.game_view.update_move(self.moves)


    def check_game_complete(self):
        pass


    def return_to_main_menu(self):
        pass


    def show_stats(self):
        print("Aquí saldrían unas estadísticas de la leche")


    def update_time(self):
        # Llama a model.update_time() para obtener el tiempo transcurrido
        elapsed_time = self.model.update_time()

        # Actualiza el tiempo en la vista
        self.game_view.update_time(elapsed_time)


    def quit_game(self):
        self.root.quit()

    
