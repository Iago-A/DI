import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox


class GameController:
    def __init__(self, root, model, main_menu, game_view):
        self.root = root
        self.model = model
        self.main_menu = main_menu
        self.game_view = game_view
        self.loading_window = None # Esta variable es para almacenar la ventana de carga y poder destruirla después.
        self.selected = [] # Variable para almacenar la posición de las carta clicadas
        self.elapsed_time = 0
        self.timer_reference = None # Variable para el timer para poder detener el after cuando se complete la partida


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

                if len(self.model.player_name) > 0:
                    return True
                else:
                    tk.messagebox.showinfo("AVISO", "No se indicó nombre de jugador.\nEl juego no se pudo iniciar.")
                    return False
            else:
                tk.messagebox.showinfo("AVISO", "La dificultad no es válida.\nEl juego no se pudo iniciar.")
                return False
        else:
            tk.messagebox.showinfo("AVISO", "No se seleccionó ninguna dificultad.\nEl juego no se pudo iniciar.")
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


    def show_loading_window(self, message):
        self.loading_window = tk.Toplevel(self.root)
        self.loading_window.title("")
        self.loading_window.geometry("200x75")
        label = tk.Label(self.loading_window, text=message)
        label.pack()

        self.loading_window.update()  # Actualiza para que se muestre de inmediato


    def check_images_loaded(self):
        print("Todas las imágenes descargadas.")
        self.loading_window.destroy()
        self.game_view.create_board(self.model)  # Crea el tablero

        # A continuación se reestablecen distintos parámetros para que se puedan jugar varias partidas seguidas.
        # Todo se resetea aquí, ya que se llaman a variables que "empiezan a existir" cuando se crea el tablero unas líneas más arriba
        # Detener temporizador previo si existiera
        self.stop_timer()

        # Reiniciar valores relacionados al tiempo
        self.elapsed_time = 0
        self.model.timer_running = False
        self.game_view.update_time(self.elapsed_time)  # Actualizar la vista para mostrar

        # Reiniciar valores del contador y parejas acertadas
        self.model.moves = 0
        self.model.currently_matches = 0

    def on_card_click(self, event, position):
        # Evitar seleccionar la misma carta dos veces
        if position in self.selected:
            return

        # Evitar interactuar con una carta ya emparejada
        if self.model.board[position[0]][position[1]]["matched"]:
            return

        # Guardar posición de la carta el self.selected
        self.selected.append(position)

        # Mostramos la imagen de la carta seleccionada temporalmente
        carta = self.model.board[position[0]][position[1]]["value"]
        self.game_view.update_board(position, self.model.images[carta])

        # Si hay dos cartas seleccionadas, comprobamos si hay coincidencia
        if len(self.selected) == 2:
            self.handle_card_selection()

        if not self.model.timer_running:
            self.model.start_timer()
            self.timer_reference = self.root.after(1000,self.update_time_continuously)  # Luego continuar actualizando cada 1000 ms

        # Actualiza el tiempo
        self.update_time()


    def update_time(self):
        # Llama a model.update_time() para obtener el tiempo transcurrido
        self.elapsed_time = self.model.update_time()

        # Actualiza el tiempo en la vista
        self.game_view.update_time(self.elapsed_time)


    def update_time_continuously(self):
        self.update_time()  # Llama a la función de actualización del label del tiempo

        # Después de 1000 ms, vuelve a llamar a esta misma función para seguir actualizando el tiempo
        self.timer_reference = self.root.after(1000,self.update_time_continuously)


    def stop_timer(self):
        if self.timer_reference is not None:
            self.root.after_cancel(self.timer_reference)
            self.timer_reference = None  # Resetear referencia
            self.model.timer_running = False


    def handle_card_selection(self):
        # Actualizar contador movimientos
        self.update_move_count()

        # Extraer las posiciones seleccionadas
        pos1, pos2 = self.selected

        # Obtener las cartas en las posiciones seleccionadas
        carta1 = self.model.board[pos1[0]][pos1[1]]["value"]
        carta2 = self.model.board[pos2[0]][pos2[1]]["value"]

        # Comprobamos si las cartas coinciden
        if carta1 == carta2:
            self.model.board[pos1[0]][pos1[1]]["matched"] = True
            self.model.board[pos2[0]][pos2[1]]["matched"] = True

            # Las cartas coinciden, las dejamos descubiertas
            self.selected = []  # Reiniciamos las seleccionadas

            self.model.currently_matches += 1

            self.check_game_complete()
        else:
            # Las cartas no coinciden, las ocultamos después de un breve retraso
            self.game_view.ventana.after(1000, lambda: self.game_view.reset_cards(pos1, pos2))
            self.selected = []  # Reiniciamos las seleccionadas


    def update_move_count(self):
        self.model.moves += 1
        self.game_view.update_move(self.model.moves)


    def check_game_complete(self):
        if self.model.currently_matches == self.model.total_matches:
            tk.messagebox.showinfo("", f"¡Juego terminado!\nMovimientos totales = {self.model.moves}\nTiempo total = {int(self.elapsed_time)}")
            self.stop_timer()
            self.return_to_main_menu()


    def return_to_main_menu(self):
        self.model.save_score()
        self.game_view.destroy()
        scores = self.model.load_scores()
        self.main_menu.show_stats(scores)


    def show_stats(self):
        scores = self.model.load_scores()
        self.main_menu.show_stats(scores)


    def quit_game(self):
        self.root.quit()

