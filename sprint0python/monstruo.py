class Monstruo:

    # Constructor
    def __init__(self, nombre, ataque, defensa, salud):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud


    # Métodos

    # Ataque del enemigo.
    def atacar(self, heroe):
        dano = self.ataque - heroe.defensa

        print("\nEl monstruo " + self.nombre + " ataca a " + heroe.nombre)

        if dano <= heroe.defensa: # El enemigo falla el ataque
            print("El héroe ha bloqueado el ataque.")
        else: # El enemigo acierta el ataque
            print("El héroe " + heroe.nombre + " ha recibido " + str(dano) + " puntos de daño.")
            heroe.salud -= dano # Se reduce la salud del héroe

            # Solo se enseñará si el heroe sigue vivo.
            if heroe.salud > 0:
                print("Salud actual: " + str(heroe.salud))


    # Se verifica que el enemigo sigue vivo para continuar el combate o no
    def esta_vivo(self):
        vivo = True

        if self.salud <= 0:
            vivo = False

        return vivo

