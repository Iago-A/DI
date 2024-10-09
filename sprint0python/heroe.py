

class Heroe:
    # Atributos
    nombre = ""


    # Constructor
    def __init__(self, nombre):
        self.nombre = nombre
        self.ataque = 20
        self.defensa = 40
        self.salud = 100
        self.salud_max = 100


    # Métodos
    def atacar(self, enemigo):
        dano = self.ataque - enemigo.defensa

        print("Héroe ataca a" + enemigo)

        if dano <= enemigo.defensa:
            print("El enemigo ha bloqueado el ataque.")
        else:
            print("El enemigo" + enemigo + "ha recibido" + dano + "puntos de daño.")


    def curarse(self):
        cura = 20
        self.salud = self.salud + cura

        if self.salud > self.salud_max:
            self.salud = self.salud_max

        print("Héroe se ha curado. Salud actual:" + str(self.salud))


    def defenderse(self):
        self.defensa = self.defensa + 5

        print("Héroe se defiende. Defensa aumentada temporalmente a" + str(self.defensa))


    def reset_defensa(self):
        self.defensa = self.defensa - 5

        print("La defensa de" + self.nombre + "vuelve a la normalidad.")


    def esta_vivo(self):
        vivo = True

        if self.salud <= 0:
            vivo = False

        return vivo


