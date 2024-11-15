import tkinter as tk
from tkinter import simpledialog


class GameView:
    def __init__(self, on_card_click_callback, update_move_count_callback, update_time_callback):
        self.ventana = None
        self.labels = {}
        self.images = {} # Diccionario para almacenar referencias a las imágenes
        self.on_card_click_callback = on_card_click_callback
        self.update_move_count_callback = update_move_count_callback
        self.update_time_callback = update_time_callback


    def set_callbacks(self, on_card_click_callback, update_move_count_callback, update_time_callback):
        self.on_card_click_callback = on_card_click_callback
        self.update_move_count_callback = update_move_count_callback
        self.update_time_callback = update_time_callback


    def create_board(self, model):
        self.ventana = tk.Toplevel()
        self.ventana.title("Partida")
        self.ventana.geometry("")

        # Cargar las imágenes desde el modelo
        self.images = model.images  # Copia el diccionario de imágenes del modelo

        hidden_image = self.images["imagen_0"]

        # Usa el tamaño de la celda para calcular la posición de cada carta
        cell_size = model.cell_size
        filas = 2
        columnas = len(model.board[0])

        i = 0
        j = 0

        for i in range(filas):
            for j in range(columnas):
                carta = model.board[i][j]

                label = tk.Label(self.ventana, image=hidden_image, width=cell_size, height=cell_size)
                label.grid(row=i, column=j, padx=5, pady=5)
                self.labels[(i, j)] = label

                # Asociar clic izquierdo del mouse a cada label
                label.bind("<Button-1>", lambda event, pos=(i, j): self.on_card_click_callback(event, pos))

        self.label_movimientos = tk.Label(self.ventana, text="Movimientos: 0")
        self.label_movimientos.grid(row=i+1, column=0, padx=5, pady=5)

        self.label_tiempo = tk.Label(self.ventana, text="Tiempo: 0")
        self.label_tiempo.grid(row=i+1, column=j, padx=5, pady=5)

        self.obtener_dimensiones_reales()
        self.centrar_ventana()


    def obtener_dimensiones_reales(self):
        self.ventana.update_idletasks()
        ancho = self.ventana.winfo_width()
        alto = self.ventana.winfo_height()
        self.ventana.geometry(f"{ancho}x{alto}")


    def centrar_ventana(self):
        self.ventana.update_idletasks()  # Asegura que las dimensiones sean correctas
        ancho = self.ventana.winfo_width()
        alto = self.ventana.winfo_height()
        x = (self.ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (alto // 2)
        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")


    def update_board(self, position, image_id):
        label = self.labels[position]
        label.config(image=image_id)


    def reset_cards(self, pos1, pos2):
        self.update_board(pos1, self.images["imagen_0"])
        self.update_board(pos2, self.images["imagen_0"])


    def update_move(self, moves):
        self.label_movimientos.config(text=f"Movimientos: {moves}")


    def update_time(self, time):
        self.label_tiempo.config(text=f"Tiempo: {int(time)}")


    def destroy(self):
        self.ventana.destroy()


class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de memoria")
        self.root.geometry("400x200")

        self.stats_window = None # Variable para el top level de stats

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
        return player_name


    def show_stats(self, stats):
        if not stats:  # Si no hay estadísticas
            stats_message = "No hay estadísticas disponibles aún."
        else:
            stats_message = stats

            # Crear una ventana para mostrar estadísticas
        self.stats_window = tk.Toplevel()
        self.stats_window.title("Estadísticas")
        self.stats_window.geometry("")

        # Crear un contenedor para los labels
        container = tk.Frame(self.stats_window)
        container.pack(expand=True, fill="both", padx=10, pady=10)

        if not stats:  # Si no hay datos
            label = tk.Label(container, text="No hay estadísticas disponibles aún.", font=("Arial", 12))
            label.pack(pady=5)
            return

        # Crear un Label por cada estadística
        for difficulty, scores in stats.items():
            # Mostrar el título de la dificultad
            difficulty_label = tk.Label(container, text=f"Dificultad: {difficulty.capitalize()}",
                                        font=("Arial", 14, "bold"))
            difficulty_label.pack(pady=5)

            if not scores:
                no_scores_label = tk.Label(container, text="Sin datos para esta dificultad.", font=("Arial", 12))
                no_scores_label.pack()
            else:
                for score in scores:
                    score_label = tk.Label(
                        container,
                        text=f"Jugador: {score['nombre']} | Movimientos: {score['movimientos']} | Fecha: {score['fecha']}",
                        font=("Arial", 12)
                    )
                    score_label.pack(anchor="w")  # Alinear el texto a la izquierda

