#Dar 5 vidas al usuario
#Dar pistas, si el numero es mayor o menor 
#Queremos poner la opción de volver a jugar generando número diferente


import random
def jugar():
    intentos = 0
    numero_aleatorio = random.randint(1,10)
    print("Bienvenido a Adivina el número")
    print("Estoy pensando en un número del 1 al 10")
    print("Adivina cual es")
    print("Solamente tienes 5 intentos")
    while intentos < 5:
        adivinanza = int(input("El número es: "))
        if adivinanza == numero_aleatorio:
            print("Adivinaste!")
            break
        elif numero_aleatorio > adivinanza:
                print("Fallaste, mi número es mayor")
        else:
                print("Fallaste, mi número es menor")
        intentos += 1 
    else:
        print("Se te acabron los intentos")
        print("Gracias por jugar")

jugar()