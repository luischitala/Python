#Dar 5 vidas al usuario
#Dar pistas, si el numero es mayor o menor 
#Queremos poner la opción de volver a jugar generando número diferente


import random
numero_aleatorio = random.randint(1,10)

print("Bienvenido a Adivina el número")
print("Estoy pensando en un número del 1 al 10")
print("Adivina cual es")
while True:
    adivinanza = int(input("El número es: "))
    if adivinanza == numero_aleatorio:
        print("Adivinaste!")
        break
    else:
        if numero_aleatorio > adivinanza:
            print("Fallaste, mi número es mayor")
        else:
            print("Fallaste, mi número es menor")

        print("Fallaste, inténtalo de nuevo")
print("Gracias por jugar")