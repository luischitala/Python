
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
        try:
            adivinanza = int(input("El número es: "))
        except ValueError:
            print("Ese no es un número válido")
        else:
                if adivinanza == numero_aleatorio:
                    print("Adivinaste!")
                    jugar_nuevamente = input("Jugar de nuevo? si/no ")
                    if jugar_nuevamente.lower() == "si":
                        jugar()
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
            jugar()


jugar()