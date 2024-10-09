import operaciones

def main():
    resp = "s"

    while resp == "s":
        num1 = filtro_numero("Inserte el primer número: ")
        num2 = filtro_numero("Inserte el segundo número: ")
        calculo(num1, num2)
        resp = pregunta()

    print("\n***FIN DE PROGRAMA***")


def filtro_numero (num):
    while True:
        try:
            return int(input(num))
        except ValueError:
            print("\nError. Se debe introducir un número.")


def calculo(num1, num2):
    print("\n***CALCULADORA***")
    print("\n1.- Sumar.")
    print("2.- Restar.")
    print("3.- Multiplicar.")
    print("4.- Dividir")
    resp = filtro_numero("\n\tOpción (1-4) ===> ")
    while resp < 1 or resp > 4:
        print("\nError. Inserte un número entre el 1 y el 4.")
        resp = filtro_numero("\n\tOpción (1-4) ===> ")

    if resp == 1:
        operaciones.suma(num1, num2)
    elif resp == 2:
        operaciones.resta(num1, num2)
    elif resp == 3:
        operaciones.multiplicacion(num1, num2)
    else:
        operaciones.division(num1, num2)


def pregunta():
    resp = input("\n¿Desea hacer más operaciones? (s/n): ").lower()
    while resp != "s" and resp != "n":
        print("Error. Solo puede introducir 's' o 'n'.")
        resp = input("\n¿Desea hacer más operaciones? (s/n): ").lower()

    return resp


if __name__ == "__main__":
    main()