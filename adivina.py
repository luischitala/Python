import random
numero_aleatorio = random.radint(1,10)

print("Bienvenido a Adivina el número")
print("Estoy pensando en un número del 1 al 10")
print("Adivina cual es")
while True:
    adivinanza = int(input("El número es: "))
    if adivinanza == numero_aleatorio:
        print("Adivinaste!")
        break
    else:
        print("Fallaste, inténtalo de nuevo")
print("Gracias por jugar")