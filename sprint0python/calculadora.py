import operaciones

def main():
    # Se inicia la variable a 's' para poder
    # entrar en el siguiente bucle
    resp = "s"

    # Si respuesta es 'no', se saldrá del buble while
    while resp == "s":
        num1 = filtro_numero("Inserte el primer número: ")
        num2 = filtro_numero("Inserte el segundo número: ")
        calculo(num1, num2) # Menú calculadora
        resp = pregunta() # Realizar otra operación o no

    print("\n***FIN DE PROGRAMA***")


# Control de que solo se inserte números y no otro caracter
def filtro_numero (num):
    while True:
        try:
            # Se intenta convertir el valor introducido a integer.
            # Si falla, es porque se insertó un caracter, y
            # se informa del error.
            return int(input(num))
        except ValueError:
            print("\nError. Se debe introducir un número.")


def calculo(num1, num2):
    # Menú
    print("\n***CALCULADORA***")
    print("\n1.- Sumar.")
    print("2.- Restar.")
    print("3.- Multiplicar.")
    print("4.- Dividir")
    resp = filtro_numero("\n\tOpción (1-4) ===> ")

    # Control de respuesta
    while resp < 1 or resp > 4:
        print("\nError. Inserte un número entre el 1 y el 4.")
        resp = filtro_numero("\n\tOpción (1-4) ===> ")

    # Elección de operación según la opción escogida
    if resp == 1:
        operaciones.suma(num1, num2)
    elif resp == 2:
        operaciones.resta(num1, num2)
    elif resp == 3:
        operaciones.multiplicacion(num1, num2)
    else:
        operaciones.division(num1, num2)


# Preguntar por más operaciones y control de que la respuesta
# solo sea 's' o 'n' y en letra minúscula
def pregunta():
    resp = input("\n¿Desea hacer más operaciones? (s/n): ").lower()

    while resp != "s" and resp != "n":
        print("Error. Solo puede introducir 's' o 'n'.")
        resp = input("\n¿Desea hacer más operaciones? (s/n): ").lower()

    return resp # Si la respuesta en 'n', se sale del bucle


if __name__ == "__main__":
    main()