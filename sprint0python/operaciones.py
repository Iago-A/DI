def main():
    print ("----MAIN INICIADO----\n")
    suma(5,15)
    resta(5, 15)
    multiplicacion(5,10)
    division (50,0)
    print ("\n----FIN DE PROGRAMA----")

def suma(num1, num2):
    print ("Suma:", num1, "+", num2, "=", num1+num2)

def resta(num1, num2):
    print ("Resta:", num1, "-", num2, "=", num1-num2)

def multiplicacion(num1, num2):
    print ("Multiplicación:", num1, "x", num2, "=", num1*num2)

def division(num1, num2):
    if num2 == 0:
        print ("No se puede dividir entre cero")
    else:
        print ("División:", num1, "/", num2, "=", num1/num2)



if __name__ == "__main__":
    main()