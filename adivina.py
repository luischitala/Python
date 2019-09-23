
#Queremos poner la opción de volver a jugar generando número diferente
import random
def jugarf():
    intentos = 0
    numero_aleatorio = random.randint(1,10)
    print("Bienvenido a Adivina el número")
    print("Estoy pensando en un número del 1 al 10")
    print("Adivina cual es")
    print("Solamente tienes 5 intentos")
    while intentos < 5:
        try:
            adivinanza = int(input("El número es: "))
        except ValueError:
            print("Ese no es un número válido")
        else:
                if adivinanza == numero_aleatorio:
                    print("Adivinaste!")
                    jugar_nuevamente = input("Jugar de nuevo? si/no ")
                    if jugar_nuevamente.lower() == "si":
                        menu()
                    else:
                        break
                elif numero_aleatorio > adivinanza:
                        print("Fallaste, mi número es mayor")
                else:
                        print("Fallaste, mi número es menor")
                intentos += 1 
                print("Intento {}/5".format(intentos))
    else:
        print("Se te acabron los intentos")
        print("Gracias por jugar")
        jugar_nuevamente = input("Jugar de nuevo? si/no ")

        if jugar_nuevamente.lower() == "si":
            menu()
def jugard():
    intentos = 0
    numero_aleatorio = random.randint(1,40)
    print("Bienvenido a Adivina el número")
    print("Estoy pensando en un número del 1 al 40")
    print("Adivina cual es")
    print("Solamente tienes 5 intentos")
    while intentos < 5:
        try:
            adivinanza = int(input("El número es: "))
        except ValueError:
            print("Ese no es un número válido")
        else:
                if adivinanza == numero_aleatorio:
                    print("Adivinaste!")
                    jugar_nuevamente = input("Jugar de nuevo? si/no ")
                    if jugar_nuevamente.lower() == "si":
                        menu()
                    else:
                        break
                elif numero_aleatorio > adivinanza:
                        print("Fallaste, mi número es mayor")
                else:
                        print("Fallaste, mi número es menor")
                intentos += 1 
                print("Intento {}/5".format(intentos))
    else:
        print("Se te acabron los intentos")
        print("Gracias por jugar")
        jugar_nuevamente = input("Jugar de nuevo? si/no ")

        if jugar_nuevamente.lower() == "si":
            menu()
def jugarl():
    intentos = 0
    numero_aleatorio = random.randint(1,10)
    print("Bienvenido a Adivina el número")
    print("Estoy pensando en un número del 1 al 10")
    print("Adivina cual es")
    print("Solamente tienes 3 intentos")
    while intentos < 3:
        try:
            adivinanza = int(input("El número es: "))
        except ValueError:
            print("Ese no es un número válido")
        else:
                if adivinanza == numero_aleatorio:
                    print("Adivinaste!")
                    jugar_nuevamente = input("Jugar de nuevo? si/no ")
                    if jugar_nuevamente.lower() == "si":
                        menu()
                    else:
                        break
                elif numero_aleatorio > adivinanza:
                        print("Fallaste, mi número es mayor")
                else:
                        print("Fallaste, mi número es menor")
                intentos += 1 
                print("Intento {}/3".format(intentos))
    else:
        print("Se te acabron los intentos")
        print("Gracias por jugar")
        jugar_nuevamente = input("Jugar de nuevo? si/no ")

        if jugar_nuevamente.lower() == "si":
            menu()
def menu():
    print()
    print("-----Bienvenido a adivina el número----")
    print("----------------------------------------")
    print("Dificultad Fácil = 1")
    print("Dificultad Difícil = 2")
    print("Dificultad Locura = 3")
    respuesta = int(input("Ingresa la dificultad deseada: "))
    print("-----------------------------------")
    if respuesta == 1:
        jugarf()
    elif respuesta == 2:
        jugard()
    elif respuesta == 3:
        jugarl()
    else:
        print("Ingresa un número válido") 
        menu()
menu()
#jugarf()