class Heroe:
    # Atributos
    nombre = ""


    # Constructor
    def __init__(self, nombre):
        self.nombre = nombre
        self.ataque = 60
        self.defensa = 20
        self.salud = 100
        self.salud_max = 100


    # Métodos

    # El usuario elige atacar
    def atacar(self, enemigo):
        dano = self.ataque - enemigo.defensa

        print("\nHéroe ataca a " + enemigo.nombre)

        if dano <= enemigo.defensa: # Ataque de héroe fallido
            print("El enemigo ha bloqueado el ataque.")
        else: # Ataque de héroe exitoso
            print("El enemigo " + enemigo.nombre + " ha recibido " + str(dano) + " puntos de daño.")
            enemigo.salud -= dano # Se reduce la salud del enemigo

        return False # Héroe no se defiende, no se restaura la defensa original


    # El usuario elige curarse
    def curarse(self):
        cura = 50
        self.salud += cura

        # Control para no curarse más de la salud máxima del héroe
        if self.salud > self.salud_max:
            self.salud = self.salud_max

        print("\nHéroe se ha curado. Salud actual: " + str(self.salud))

        return False # Héroe no se defiende, no se restaura la defensa original


    # El usuario elige defenderse
    def defenderse(self):
        self.defensa += 5

        print("\nHéroe se defiende. Defensa aumentada temporalmente a " + str(self.defensa))

        return True # Héroe sí se defiende, se restaurará la defensa original después de que el enemigo ataque


    # Se restaura la defensa original después del ataque del enemigo. solo si el usuario se defendió previamente
    def reset_defensa(self):
        self.defensa -= 5

        print("La defensa de " + self.nombre + " vuelve a la normalidad.")


    # Se controla que el héroe siga vivo para continuar el juego o no
    def esta_vivo(self):
        vivo = True

        if self.salud <= 0:
            vivo = False

        return vivo


