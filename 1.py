
def realizar_operacion(operacion,numero1,numero2):
    if operacion == 1:
        return numero1 + numero2
    elif operacion == 2:
        return numero1 - numero2
    elif operacion == 3:
        return numero1 * numero2
    else:
        return numero1 / numero2

print("Bienvenido a la calculadora")
while True:
    print("Estas son las operaciones que puedes realizar:")
    print("1 - Suma")
    print("2 - Resta")
    print("3 - Multiplicación")
    print("4 - División")

    try:
        operacion = int(input("Introduce el Número de operación deseado: "))
        numero1 = int(input("Introduce el primer número: "))
        numero2 = int(input("Introduce el segundo número: "))
    except ValueError:
        print("Por favor ingrese un número válido")
    else:
        if operacion < 1 or operacion > 4:
            print("Ese no es un número de operacion válido")
            continue
        resultado = realizar_operacion(operacion, numero1, numero2)
        print("El resultado es: " str(resultado))
        continuar = input("Deseas continuar? si/no")
        print()
        print()
        if continuar != "si":
            break
print("Gracias por usar nuestra calculadora!")