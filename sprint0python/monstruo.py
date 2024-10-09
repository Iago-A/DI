class Monstruo:

    # Constructor
    def __init__(self, nombre, ataque, defensa, salud):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud


    # Métodos
    def atacar(self, heroe):
        dano = self.ataque - heroe.defensa

        print("El monstruo" + self.nombre + "ataca a" + heroe.nombre)

        if dano <= heroe.defensa:
            print("El héroe ha bloqueado el ataque.")
        else:
            print("El héroe" + self.nombre + "ha recibido" + dano + "puntos de daño.")


    def esta_vivo(self):
        vivo = True

        if self.salud <= 0:
            vivo = False

        return vivo

