import random
import tkinter as tk
from tkinter import messagebox


class RockPaperSeasorGame:
    def __init__(self, root):
        self.root = root
        self.root.title("¡Piedra, papel, tijera!")
        self.root.geometry("370x450")


        # Contadores de puntos
        self.player1_score = 0
        self.player2_score = 0


        # Tipo de juego escogido
        self.game_type = 1


        # Control de quién está jugando y opciones escogidas
        self.who_is_playing = "Jugador 1"
        self.player1_value = ""
        self.player2_value = ""


        # Menú principal
        self.main_menu = tk.Menu(self.root)
        self.root.config(menu=self.main_menu)


        # Submenú
        self.options_menu = tk.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="Jugar", menu=self.options_menu)
        self.options_menu.add_command(label="Jugador vs Máquina", command=self.versus_cpu)
        self.options_menu.add_separator()
        self.options_menu.add_command(label="Jugador vs Jugador", command=self.versus_player)

        self.exit = tk.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label="Salir", menu=self.exit)
        self.exit.add_command(label="Salir", command=self.close_app)


        # Etiqueta contador
        self.counter = tk.Label(self.root, text="", font=("Arial", 20))
        self.counter.grid(row=0, column=1, pady=30, sticky="nsew")


        # Botones
        self.rock_button = tk.Button(self.root, text="", width=10, command=lambda: self.player_selection("Rock"))
        self.rock_button.grid(row=1, column=0, padx=5, pady=30, sticky="nsew")
        # Ocultar el botón temporalmente
        self.rock_button.grid_remove()

        self.papper_button = tk.Button(self.root, text="", width=10, command=lambda: self.player_selection("Paper"))
        self.papper_button.grid(row=1, column=1, padx=5, pady=30, sticky="nsew")
        # Ocultar el botón temporalmente
        self.papper_button.grid_remove()

        self.seasor_button = tk.Button(self.root, text="", width=10, command=lambda: self.player_selection("Seasor"))
        self.seasor_button.grid(row=1, column=2, padx=5, pady=30, sticky="nsew")
        # Ocultar el botón temporalmente
        self.seasor_button.grid_remove()

        self.player1_button = tk.Button(self.root, text="", width=10, command=self.save_player1_selection)
        self.player1_button.grid(row=2, column=0, padx=5, sticky="nsew")
        # Ocultar el botón temporalmente
        self.player1_button.grid_remove()

        self.play_button = tk.Button(self.root, text="", width=10, command=self.play)
        self.play_button.grid(row=2, column=1, padx=5, sticky="nsew")
        # Ocultar el botón temporalmente
        self.play_button.grid_remove()

        self.player2_button = tk.Button(self.root, text="", width=10, command=self.save_player2_selection)
        self.player2_button.grid(row=2, column=2, padx=5, sticky="nsew")
        # Ocultar el botón temporalmente
        self.player2_button.grid_remove()


        # Etiquetas juego
        self.player1_message = tk.Label(self.root, text="", font=("Arial", 10, "bold"))
        self.player1_message.grid(row=3, column=0, pady=30, sticky="nsew")

        self.player2_message = tk.Label(self.root, text="", font=("Arial", 10, "bold"))
        self.player2_message.grid(row=3, column=2, pady=30, sticky="nsew")

        self.player1_choice = tk.Label(self.root, text="")
        self.player1_choice.grid(row=4, column=0, sticky="nsew")

        self.vs_label = tk.Label(self.root, text="")
        self.vs_label.grid(row=4, column=1, sticky="nsew")

        self.player2_choice = tk.Label(self.root, text="")
        self.player2_choice.grid(row=4, column=2, sticky="nsew")

        self.winner_label = tk.Label(self.root, text="", font=("Arial", 10))
        self.winner_label.grid(row=5, column=1, pady=20, sticky="nsew")


        # Configurar la expansión de las filas y columnas
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_rowconfigure(5, weight=1)


    # Se ejecuta al seleccionar en el menú el modo de juego vs CPU
    def versus_cpu(self):
        self.reset_game()
        self.game_type = 1
        # Ocultar botones del otro modo de juego
        self.player1_button.grid_remove()
        self.player2_button.grid_remove()
        self.show_interface()


    # Se ejecuta al seleccionar en el menú el modo de juego jugador vs jugador
    def versus_player(self):
        # Empezar por turno de jugador 1 y activar su botón de guardado
        self.who_is_playing = "Jugador 1"
        self.player1_button.config(state="active")

        self.reset_game()
        self.game_type = 2
        self.show_interface()


    def close_app(self):
        self.root.quit()


    # Mostrar widgets en la ventana
    def show_interface(self):
        self.show_buttons()
        self.counter.config(text="0 | 0")
        self.rock_button.config(text="Piedra")
        self.papper_button.config(text="Papel")
        self.seasor_button.config(text="Tijera")
        self.play_button.config(text="Jugar")
        self.player1_message.config(text="Jugador 1")
        self.vs_label.config(text="VS")

        # Modo seleccionado vs CPU
        if self.game_type == 1:
            self.player2_message.config(text="CPU")
        # Modo seleccionado jugador vs jugador
        else:
            self.player1_button.config(text="Guardar jugada\n jugador 1")
            self.player2_button.config(text="Guardar jugada\n jugador 2")
            self.player2_message.config(text="Jugador 2")


    def show_buttons(self):
        self.rock_button.grid()
        self.papper_button.grid()
        self.seasor_button.grid()
        self.play_button.grid()

        # Al seleccionar modo de juego jugador vs jugador
        if self.game_type == 2:
            self.player1_button.grid()
            self.player2_button.grid()
            self.player2_button.config(state="disabled")


    # Sirve para mostrar la selección de los jugadores o CPU en las etiquetas correspondientes
    def player_selection(self, option):
        # Modo de juego jugador vs CPU
        if self.game_type == 1:
            # Poner en blanco la selección de la CPU
            self.player2_choice.config(text="")

            value = self.game_values(option)
            self.player1_choice.config(text=f"{value}")

        # Modo de juego jugador vs jugador
        else:
            value = self.game_values(option)
            if self.who_is_playing == "Jugador 1":
                self.player1_choice.config(text=f"{value}")
            else:
                self.player2_choice.config(text=f"{value}")


    def game_values(self, option):
        if option == "Rock":
            return "Piedra"
        elif option == "Paper":
            return "Papel"
        else:
            return "Tijera"


    # Se activa al pulsar el botón de jugar
    def play(self):
        # Modo de juego jugador vs CPU
        if self.game_type == 1:
            # Selección del jugador 1
            self.player1_value = self.player1_choice.cget("text")

            if self.player1_value != "":
                # Selección aleatoria del ordenador
                self.player2_value = self.cpu_selection()
                self.player2_choice.config(text=self.player2_value)

                self.show_results()
            else:
                messagebox.showinfo("Aviso", "Debe seleccionar piedra, papel o tijera antes de jugar.")

        # Modo de juego jugador vs jugador
        else:
            # Selección del jugador 1 y 2 es realizada en otra función al pulsar los botones de guardado correspondientes

            if self.player1_value != "" and self.player2_value != "":
                self.show_results()
            else:
                messagebox.showinfo("Aviso", "Ambos jugadores deben seleccionar piedra, papel, o tijera, y guardar sus jugadas en sus respectivas casillas antes de jugar.")

        # Actualizar marcador
        self.counter.config(text=f"{self.player1_score} | {self.player2_score}")

        # Fin de la partida
        if self.player1_score == 3:
            self.winner_messagebox(1)
        if self.player2_score == 3:
            self.winner_messagebox(2)


    def cpu_selection(self):
        self.list = ["Piedra",
                     "Papel",
                     "Tijera"]
        cpu_choice = random.choice(self.list)

        return cpu_choice


    def show_results(self):
        # Resultados
        if self.player1_value == self.player2_value:
            self.winner_label.config(text="Empate")
        elif (self.player1_value == "Piedra" and self.player2_value == "Tijera") or \
                (self.player1_value == "Papel" and self.player2_value == "Piedra") or \
                (self.player1_value == "Tijera" and self.player2_value == "Papel"):
            self.winner_label.config(text="¡Jugador gana!")
            self.player1_score += 1
        else:
            if self.game_type == 1:
                self.winner_label.config(text="CPU gana")
            else:
                self.winner_label.config(text="¡Jugador 2 gana!")
            self.player2_score += 1


    def winner_messagebox(self, code):
        # Si gana el jugador 1
        if code == 1:
            if self.game_type == 1:
                messagebox.showinfo("", "¡Has ganado al mejor de 3 rondas!")
            else:
                messagebox.showinfo("", "¡Jugador 1 gana al mejor de 3!")
            self.reset_game()
        # Si gana la CPU o el jugador 2
        else:
            if self.game_type == 1:
                messagebox.showinfo("", "CPU ha ganado al mejor de 3 rondas.")
            else:
                messagebox.showinfo("", "¡Jugador 2 gana al mejor de 3!")
            self.reset_game()


    def reset_game(self):
        self.player1_score = 0
        self.player2_score = 0

        self.player1_value = ""
        self.player2_value = ""

        # Restablecer la interfaz al comienzo del juego
        self.show_interface()
        self.winner_label.config(text="")
        self.player1_choice.config(text="")
        self.player2_choice.config(text="")


    # Se activa al pulsar botón de guardado del jugador 1
    def save_player1_selection(self):
        # Guardar el valor seleccionado de la etiqueta de juego
        self.player1_value = self.player1_choice.cget("text")
        # "Ocultar" la selección al otro jugador
        self.player1_choice.config(text="")
        # Deshabilitar el botón de guardado y activar el del otro jugador
        self.player1_button.config(state="disabled")
        self.player2_button.config(state="active")
        # Pasarle el turno al otro jugador
        self.who_is_playing = "Jugador 2"


    # Se activa al pulsar botón de guardado del jugador 2
    def save_player2_selection(self):
        # Guardar el valor seleccionado de la etiqueta de juego
        self.player2_value = self.player2_choice.cget("text")
        # "Ocultar" la selección al otro jugador
        self.player2_choice.config(text="")
        # Deshabilitar el botón de guardado y activar el del otro jugador
        self.player2_button.config(state="disabled")
        self.player1_button.config(state="active")
        # Pasarle el turno al otro jugador
        self.who_is_playing = "Jugador 1"


if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperSeasorGame(root)
    root.mainloop()