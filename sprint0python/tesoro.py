import random


class Tesoro:

    # Constuctor
    def __init__(self):
        # La siguiente variable es una lista de las posibles recompensas
        self.beneficios = [
            "Poción de ataque",
            "Poción de defensa",
            "Poción de salud"
        ]


    # Métodos

    # El tesoro se genera de manera aleatoria con random.choice('lista de recompensas')
    def encontrar_tesoro(self, heroe):
        elemento_aleatorio = random.choice(self.beneficios)
        print("\nEl héroe ha encontrado un tesoro: " + elemento_aleatorio)

        # Se aplica una mejora u otra dependiendo del tesoro
        if elemento_aleatorio == "Poción de ataque":
            heroe.ataque += 2
            print("\nEl ataque de " + heroe.nombre + " aumenta a " + str(heroe.ataque))
            input("\n\t<Pulse intro para avanzar>")  # Se añade una pausa
        elif elemento_aleatorio == "Poción de defensa":
            heroe.defensa += 2
            print("\nLa defensa de " + heroe.nombre + " aumenta a " + str(heroe.defensa))
            input("\n\t<Pulse intro para avanzar>")  # Se añade una pausa
        else:
            heroe.salud = heroe.salud_max
            print("\nLa salud de " + heroe.nombre + " ha sido restaurada a " + str(heroe.salud_max))
            input("\n\t<Pulse intro para avanzar>")  # Se añade una pausa