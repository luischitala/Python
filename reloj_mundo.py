import datetime
print("Bienvenido al Reloj del Mundo")

def mostrar_menu():
   
    print("Estas son las operaciones qe puedes realizar: ")
    print("1 Ver la hora")
    print("2 Ver la fecha y hora")
    print("3 ver la hora en Nueva York")
    print("4 Ver la hora en San Francisco")
    print("5 Ver las instrucciones nuevamente")
    print("6 Para salir")

def ver_hora():
    time_zone = datetime.timezone(datetime.timedelta(hours=-6))
    hora_actual = datetime.datetime.now(time_zone).time()
    print(hora_actual)
def ver_reloj():
    while True:
        operacion = input(": ")
        
        if operacion == "1":
            ver_hora()
        elif operacion == "2":
            print(datetime.datetime.now())
        elif operacion == "3":
            print("Hora en Nueva York")
        elif operacion == "4":
            print("Hora en San Francisco")
        elif operacion == "5":
            mostrar_menu()
        elif operacion == "6":
            break
        else:
            print("Ingrese una opción válida")
            print()
            print()
            print()
            print()

            mostrar_menu()

mostrar_menu()
ver_reloj()