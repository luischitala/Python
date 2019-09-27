import datetime
print("Bienvenido al Reloj del Mundo")

def mostrar_menu():
   
    print("Estas son las operaciones qe puedes realizar: ")
    print("1 Ver la hora")
    print("2 Ver la fecha y hora")
    print("3 ver la hora en Nueva York")
    print("4 Ver la hora en Japón")
    print("5 Ver la hora en Francia")
    print("6 Ver la hora en San Francisco")
    print("7 Ver las instrucciones nuevamente")
    print("8 Para salir")

def ver_hora(zona_horaria):
    if zona_horaria == -6:
        zona = "Tiempo Central"
    elif zona_horaria == -8:
        zona = "Tiempo del Pacífico"
    elif zona_horaria == +9:
        zona = "en Japón"
    elif zona_horaria == +2:
        zona = "en Francia"
    else:
        zona = "Tiempo del Este"

    formato = "%H:%M:%S %p"
    zona_horaria = datetime.timezone(datetime.timedelta(hours=zona_horaria))
    hora_actual = datetime.datetime.now(zona_horaria).time()
    hora_formateada = hora_actual.strftime(formato)
    print("La hora exacta en {} es: {}".format(zona,hora_formateada))
def ver_fecha_hora():
    formato = "%B, %d, %Y"
    zona_horaria = datetime.timezone(datetime.timedelta(hours=-6))
    fecha_actual = datetime.datetime.now(zona_horaria)
    fecha_formateada = fecha_actual.strftime(formato)
    print("La fecha es: {}".format(fecha_formateada))
def ver_reloj():
    while True:
        operacion = input(": ")
        if operacion == "1":
            ver_hora(-6)
        elif operacion == "2":
            ver_fecha_hora()
        elif operacion == "3":
            ver_hora(-5)
        elif operacion == "4":
            ver_hora(+9)
        elif operacion == "5":
            ver_hora(+2)
        elif operacion == "6":
            ver_hora(-8)
        elif operacion == "7":
            mostrar_menu()
        elif operacion == "8":
            break
        else:
            print("Ingrese una opción válida")
            print()
            print()
            print()
            print()

            mostrar_menu()
    print("Gracias por utilizar el reloj Mundial")

mostrar_menu()
ver_reloj()