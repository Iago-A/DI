import random


class Tesoro:

    # Constuctor
    def __init__(self):
        # La siguiente variable es una lista
        self.beneficios = ["Poción de ataque", "Poción de defensa", "Poción de salud"]


    # Métodos
    def encontrar_tesoro(self, heroe):
        elemento_aleatorio = random.choice(self.beneficios)
        print("El héroe ha encontrado un tesoro:" + elemento_aleatorio)

        if elemento_aleatorio == "Poción de ataque":
            heroe.ataque += 5
            print("\nEl ataque de" + heroe.nombre + "aumenta a" + heroe.ataque)
        elif elemento_aleatorio == "Poción de defensa":
            heroe.defensa += 5
            print("\nLa defensa de" + heroe.nombre + "aumenta a" + heroe.defensa)
        else:
            heroe.salud = heroe.salud_max
            print("\nLa salud de" + heroe.nombre + "ha sido restaurada a" + heroe.salud_max)