import time

from monstruo import Monstruo
from tesoro import Tesoro
import random

class Mazmorra:

    # Constructor
    def __init__(self, heroe):
        self.heroe = heroe
        # Lista de enemigos. Es más complicado para que suponga un desafio al jugador es el 'Esqueleto oscuro'.
        # Si se desea poner más facil, reducir su ataque y su defensa, por ejemplo, en 5 puntos
        self.monstruos = [
            Monstruo("Slim de caverna", 42, 20, 80),
            Monstruo("Esqueleto", 45, 20, 140),
            Monstruo("Sombra", 44, 20, 80),
            Monstruo("Araña", 58, 25, 100),
            Monstruo("Esqueleto oscuro", 65, 30, 180)
        ]
        self.tesoro = Tesoro


    # Métodos

    # Se inicia el juego
    def jugar(self):
        # Atributo para saber si el heroe se defiende o no
        defendiendose = False

        print("\nHéroe entra en la mazmorra.")

        # Mientras el héroe tenga salud, y no se haya derrotado a todos los enemigos, el juego continua
        while self.heroe.esta_vivo() and len(self.monstruos) > 0:

            # Fase de avance, nuevo enemigo
            monstruo = random.choice(self.monstruos) # Aquí se elige uno de los enemigos de forma aleatoria, y se guarda en la variable monstruo
            print("\nTe has encontrado con un " + monstruo.nombre)
            input("\n\t<Pulse intro para empezar el combate>")  # Se añade una pausa

            # Fase de combate
            # Mientras enemigo y héroe estén vivos, se decide acción de combate
            while monstruo.esta_vivo() and self.heroe.esta_vivo():
                defendiendose = self.enfrentar_enemigo(monstruo)
                input("\n\t<Pulse intro para terminar el turno>")  # Se añade una pausa

                # Si el enemigo aún no fue derrotado, atacará al usuraio
                if monstruo.esta_vivo():
                    monstruo.atacar(self.heroe)

                    # Si el héroe sigue vivo, hay un nuevo turno
                    if self.heroe.salud > 0:
                        input("\n\t<Pulse intro para terminar el turno>")  # Se añade una pausa

                    # Si previamente nos hemos defendido y seguimos vivos, se restaura la defensa al estado original
                    if defendiendose and self.heroe.salud > 0:
                        # Se devuelve la defensa al estado original
                        self.heroe.reset_defensa()
                        defendiendose = False

                # Si el enemigo fue derrotado tras el ataque del héroe, no puede devolver el ataque y se termina el combate
                else:
                    print("\nEl monstruo " + monstruo.nombre + " ha sido derrotado.")
                    input("\n\t<Pulse intro para avanzar>") # Se añade una pausa

                    # Eliminamos al monstruo de la lista para que esta cada vez sea más pequeña
                    self.monstruos.remove(monstruo)

                    # Si aún quedan monstruos se busca un tesoro, de lo contrario no, porque el juego ya se termina
                    if len(self.monstruos) > 0:
                        self.buscar_tesoro()

        # Final de la mazmorra, si el héroe no tiene salud se pierde. Si se llega con salud a este punto, es porque no quedan
        # más enemigos, y el usuario gana.
        if not self.heroe.esta_vivo(): # Game over
            print("\nHéroe ha sido derrotado en la mazmorra.")
        else: # Victoria
            print("\n¡"+ self.heroe.nombre + " ha derrotado a todos los monstruos y ha conquistado la mazmorra!")


    #Menú con opciones de combate
    def enfrentar_enemigo(self, enemigo):
        resp = 0 # Respuesta en 0 para poder entrar al bucle

        while resp < 1 or resp > 3:
            print("\n¿Qué deseas hacer?")
            print("\n1. Atacar")
            print("2. Defender")
            print("3. Curarse")
            resp = input("\nSeleccione opción (1-3): ")
            # Control de que se inserte un número y no un caracter
            try:
                resp = int(resp)
            except ValueError:
                resp = 0

            # Control de número dentro del límite
            if resp < 1 or resp > 3:
                print("Opción no válida.")

        # Se escoge acción dependiendo de la opción que el usuario haya elegido
        if resp == 1: # Atacar
            defendiendose = self.heroe.atacar(enemigo)
        elif resp == 2: # Defender
            defendiendose = self.heroe.defenderse()
        else:   # Curar
            defendiendose = self.heroe.curarse()

        return defendiendose

    # La busqueda de tesoro se ejecuta tras vencer al enemigo y si aún no se terminó la mazmorra
    def buscar_tesoro(self):

        print("\nBuscando tesoro...")
        time.sleep(2) # Pausa de 2 segundos
        print("Buscando tesoro...")
        time.sleep(2)  # Pausa de 2 segundos

        tesoro = Tesoro()
        tesoro.encontrar_tesoro(self.heroe) # En el metodo se elige tesoro aleatorio