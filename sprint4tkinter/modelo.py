import random
import threading
import time
import os
from datetime import datetime

from recursos import descargar_imagen


class GameModel:
    def __init__(self, difficulty, player_name, cell_size=100):
        self.difficulty = difficulty
        self.player_name = player_name
        self.cell_size = cell_size
        self.board = [] # Aquí se guarda el tablero
        self.images = {}  # Diccionario para almacenar las imágenes descargadas
        self.start_time = None  # Variable para almacenar la hora de inicio del juego
        self.elapsed_time = 0
        self.timer_running = False
        self.moves = 0
        self.total_matches = 0 # Variable de aciertos necesarios para terminar
        self.currently_matches = 0
        self.score_file = "ranking.txt" # Fichero de estadísticas


    # Se establece el número de pares de cartas según la dificultad
    def _generate_board(self):
        if self.difficulty == "fácil":
            num_pares = 3
        elif self.difficulty == "medio":
            num_pares = 5
        else:
            num_pares = 10

        self.total_matches = num_pares

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
        self.board = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                valor = cartas.pop(0)  # Obtén el siguiente valor para la carta
                fila.append({"value": valor, "matched": False})  # Usamos un diccionario para cada carta
            self.board.append(fila)


    def _load_images(self):
        size = 100
        urls = {
            "imagen_0": "https://github.com/Iago-A/DI/blob/main/sprint4tkinter/Cartas/cartas_oculta.jpg?raw=true",
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

        def load_images_thread():
            for clave, url in urls.items():

                self.images[clave] =  descargar_imagen(url,(size,size))
        threading.Thread(target = load_images_thread(), daemon = True).start()


    def start_timer(self):
        self.start_time = time.time()  # Guarda el tiempo actual como inicio
        self.timer_running = True


    def update_time(self):
        if self.timer_running:
            # Calcula el tiempo transcurrido
            self.elapsed_time = time.time() - self.start_time
        return self.elapsed_time


    def save_score(self):
        # Crear una estructura para almacenar puntuaciones
        scores = {
            "fácil": [],
            "medio": [],
            "difícil": [],
        }

        # Leer el archivo de puntuaciones si existe
        if os.path.exists(self.score_file):
            with open(self.score_file, "r") as archivo:
                for linea in archivo:
                    nombre, dificultad, movimientos, fecha = linea.strip().split(" | ")
                    scores[dificultad].append({
                        "nombre": nombre,
                        "movimientos": int(movimientos),
                        "fecha": fecha
                    })

        # Agregar la nueva puntuación
        nueva_puntuacion = {
            "nombre": self.player_name,
            "movimientos": self.moves,
            "fecha": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }
        scores[self.difficulty].append(nueva_puntuacion)

        # Ordenar las puntuaciones de cada dificultad por movimientos (ascendente)
        for dificultad in scores:
            scores[dificultad].sort(key=lambda x: x["movimientos"])
            # Conservar solo las tres mejores puntuaciones
            scores[dificultad] = scores[dificultad][:3]

        # Guardar las puntuaciones de vuelta al archivo
        with open(self.score_file, "w") as archivo:
            for dificultad, lista_puntuaciones in scores.items():
                for puntuacion in lista_puntuaciones:
                    archivo.write(
                        f'{puntuacion["nombre"]} | {dificultad} | {puntuacion["movimientos"]} | {puntuacion["fecha"]}\n')


    def load_scores(self):
        # Crear una estructura para almacenar puntuaciones
        scores = {
            "fácil": [],
            "medio": [],
            "difícil": [],
        }

        # Leer el archivo de puntuaciones si existe
        if os.path.exists(self.score_file):
            with open(self.score_file, "r") as archivo:
                for linea in archivo:
                    nombre, dificultad, movimientos, fecha = linea.strip().split(" | ")
                    scores[dificultad].append({
                        "nombre": nombre,
                        "movimientos": int(movimientos),
                        "fecha": fecha
                    })

        return scores