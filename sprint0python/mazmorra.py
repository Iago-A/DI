import monstruo
from monstruo import Monstruo
from tesoro import Tesoro
import random

class Mazmorra:

    # Constructor
    def __init__(self, heroe):

        self.heroe = heroe
        self.monstruos = [Monstruo("Slim de caverna", 5, 2, 20), Monstruo("Esqueleto", 15, 20, 30),
                          Monstruo("Sombra", 10, 40, 20), Monstruo("Araña", 20, 30, 40),
                          Monstruo("Esqueleto oscuro", 30, 40, 60)]
        self.tesoro = Tesoro


    # Métodos
    def jugar(self):

        print("\nHéroe entra en la mazmorra.")

        while self.heroe.esta_vivo() and len(self.monstruos) > 0:
            monstruo = random.choice(self.monstruos)
            print("\nTe has encontrado con un " + monstruo.nombre)

            # Fase de acción
            self.enfrentar_enemigo(monstruo)

            if monstruo.esta_vivo():
                monstruo.atacar(self.heroe)
            else:
                print("\nEl monstruo" + monstruo.nombre + "ha sido derrotado.")
                self.buscar_tesoro()
                # Eliminamos al monstruo de la lista para que esta cada vez sea más pequeña
                self.monstruos.remove(monstruo)

        if not self.heroe.esta_vivo(self.heroe):
            print("Héroe ah sido derrotado en la mazmorra.")
        else:
            print("¡"+ self.heroe.nombre + "ha derrotado a todos los monstruos y ha conquistado la mazmorra!")


    def enfrentar_enemigo(self, enemigo):
        resp = 0

        while resp < 1 or resp > 3:
            print("\n¿Qué deseas hacer?")
            print("\n1. Atacar")
            print("2. Defender")
            print("3. Curarse")
            resp = input("\nSeleccione opción (1-3): ")
            # Control de número
            try:
                int(resp)
            except ValueError:
                print("Opción no válida.")
                resp = 0

            # Control de número dentro del límite
            if resp < 1 or resp > 3:
                print("Opción no válida.")

        if resp == 1:
            self.heroe.atacar(monstruo)
        elif resp == 2:
            self.heroe.defenderse()
        else:
            self.heroe.curarse()


    def buscar_tesoro(self):

        print("\nBuscando tesoro...")

        tesoro = Tesoro()
        tesoro.encontrar_tesoro(self.heroe)