
#debemos hacer funcion de diferencia
#debemos hacer funcion de diferencia simetrica
def union_conjuntos(conjunto_a,conjunto_b):
    print()
    print("La unión de A y B es: {}".format(conjunto_a.union(conjunto_b)))
    print()


def interseccion_conjuntos(conjunto_a,conjunto_b):
    print()
    print("La intersección de A y B es: {}".format(conjunto_a.intersection(conjunto_b)))
    print()

def diferencia_conjuntos(conjunto_a,conjunto_b):
    print("Elije la diferencia que quieres reaizar: ")
    print("1 A - B")
    print("2 B - A")
    try:
        operacion = int(input(":  "))
    except ValueError:
        print("\nIntroduce 1 o 2 primo\n")
        diferencia_conjuntos(conjunto_a,conjunto_b)
    else:
        if operacion == 1:
            print("La diferencia de A y B es: {}".format(conjunto_a.difference(conjunto_b)))
        elif operacion == 2:
            print("La diferencia de B y A es: {}".format(conjunto_b.difference(conjunto_a)
            ))
        else:
            print("No reconozco esa operación. Intenta de nuevo")
            diferencia_conjuntos(conjunto_a,conjunto_b)
        print()

def diferencia_simetrica_conjuntos(conjunto_a,conjunto_b):
    print()
    print("La diferencia simetrica de A y B es: {}".format(conjunto_a.symmetric_difference(conjunto_b)))
    print()

def ver_instrucciones():
    print("Operaciones que puedes realizar: ")
    print("1 - Union")
    print("2 - Intersección")
    print("3 - Diferencia")
    print("4 - Diferencia simétrica")
    print("5 - Ver instrucciones")
    print("6 - Salir")


def calculadora_conjuntos():
    print("Bienvenido a los Conjuntos")
    print("Introduce los elementos de los conjuntos, separados por espacios")
    print("Ejemplo: 1 3 4 5 6")

    conjunto_a = set(input("Conjunto A: ").split())
    conjunto_b = set(input("Conjunto B: ").split())
    ver_instrucciones()


    while True:
        try:
            operacion = int(input(":"))
        except ValueError:
            print("Introduce un número del 1 al 6")
        else:
            if operacion == 1:
                union_conjuntos(conjunto_a,conjunto_b)
            elif operacion == 2:
                interseccion_conjuntos(conjunto_a,conjunto_b)
            elif operacion == 3:
                diferencia_conjuntos(conjunto_a,conjunto_b)
            elif operacion == 4:
                diferencia_simetrica_conjuntos(conjunto_a,conjunto_b)
            elif operacion == 5:
                ver_instrucciones()
            elif operacion == 6:
                print("Gracias por utilizar nuestra aplicación, te esperamos pronto")
                break
            else:
                print("No reconozco esa operación, Intenta de nuevo primo")

calculadora_conjuntos()
