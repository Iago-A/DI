import random

from recursos import descargar_imagen


class GameModel:
    def __init__(self, difficulty, player_name, cell_size=100):
        self.difficulty = difficulty
        self.player_name = player_name
        self.cell_size = cell_size
        self.board = [] # Aquí se guarda el tablero
        self.images = {}  # Diccionario para almacenar las imágenes descargadas
        self.images_loaded = False  # Flag para saber si las imágenes están cargadas
        self.total_images = 10  # Total de imágenes que necesitamos cargar
        self.loaded_images = 0  # Contador de imágenes descargadas


    # Se establece el número de pares de cartas según la dificultad
    def _generate_board(self):
        if self.difficulty == "fácil":
            num_pares = 3
        elif self.difficulty == "medio":
            num_pares = 5
        else:
            num_pares = 10

        cartas_disponibles = ["imagen_1", "imagen_2", "imagen_3", "imagen_4", "imagen_5",
                  "imagen_6", "imagen_7", "imagen_8", "imagen_9", "imagen_10"]

        # Seleccionamos solo la cantidad de cartas necesarias según la dificultad
        cartas_seleccionadas = cartas_disponibles[:num_pares]

        # Creamos una lista de cartas duplicadas para hacer los pares
        cartas = cartas_seleccionadas * 2  # Cada carta aparece dos veces

        # Mezclamos las cartas aleatoriamente
        random.shuffle(cartas)

        # Determinamos las dimensiones del tablero
        filas = 2
        columnas = num_pares

        # Creamos las 2 filas con las cartas seleccionadas
        self.board = [cartas[i * columnas:(i + 1) * columnas] for i in range(filas)]

        # Imprimir el tablero generado para comprobar
        for fila in self.board:
            print(fila)

    def _load_images(self):
        size = 300
        urls = {
            "imagen_1": "https://github.com/Iago-A/DI/blob/main/sprint4tkinter/Cartas/10%20picas.jpg?raw=true",
            "imagen_2": "https://github.com/Iago-A/DI/blob/main/sprint4tkinter/Cartas/2%20treboles.jpg?raw=true",
            "imagen_3": "https://github.com/Iago-A/DI/blob/main/sprint4tkinter/Cartas/3%20diamantes.jpg?raw=true",
            "imagen_4": "https://github.com/Iago-A/DI/blob/main/sprint4tkinter/Cartas/4%20picas.jpg?raw=true",
            "imagen_5": "https://github.com/Iago-A/DI/blob/main/sprint4tkinter/Cartas/6%20corazones.jpg?raw=true",
            "imagen_6": "https://github.com/Iago-A/DI/blob/main/sprint4tkinter/Cartas/7%20diamantes.jpg?raw=true",
            "imagen_7": "https://github.com/Iago-A/DI/blob/main/sprint4tkinter/Cartas/as%20trevoles.jpg?raw=true",
            "imagen_8": "https://github.com/Iago-A/DI/blob/main/sprint4tkinter/Cartas/jota%20corazones.jpg?raw=true",
            "imagen_9": "https://github.com/Iago-A/DI/blob/main/sprint4tkinter/Cartas/reina%20corazones.jpg?raw=true",
            "imagen_10": "https://github.com/Iago-A/DI/blob/main/sprint4tkinter/Cartas/rey%20picas.jpg?raw=true",
        }

        # Función callback que se llama cuando una imagen se descarga
        def on_image_loaded(imagen_tk):
            self.images[nombre] = imagen_tk  # Guardamos la imagen descargada en el diccionario
            self.loaded_images += 1  # Aumentamos el contador de imágenes cargadas
            if self.loaded_images == self.total_images:
                self.images_are_loaded()  # Si todas están cargadas, marcamos como cargadas

        # Descargamos las imágenes y pasamos el callback
        for nombre, url in urls.items():
            self.images[nombre] = descargar_imagen(url, size, on_image_loaded)


    def images_are_loaded(self):
        print("Descarga de imágenes completada")
        self.images_loaded = True  # Cuando las imágenes estén descargadas, actualizamos el flag


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
