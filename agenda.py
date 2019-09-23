#Agregar un contacto
#Remover contactos
#Actualizar contactos
#Ver un contacto
#Ver todos nuestros contactos

agenda_telefonica = dict()
def imprimir_operacion(nombre_operacion):
    print()
    print("---------Agenda Telefónica-------------")
    print(nombre_operacion)
    print("---------------------------------------------")
    print()


def agregar_contacto():
    nombre = input("Nombre del nuevo Contacto: ")
    numero = input("Número del nuevo Contacto: ")
    agenda_telefonica[nombre] = numero
    imprimir_operacion("Contacto Agregado")


def remover_contacto():
    print()
    nombre = input("Nombre del contacto que deseas Borrar: ")
    nombre_operacion = None
    try:
        del agenda_telefonica[nombre]
    except KeyError:
        nombre_operacion = "Ese contacto no existe"
    else:
        nombre_operacion = "Contacto borrado"
    imprimir_operacion(nombre_operacion)


def actualizar_contacto():
   nombre = input("Nombre del Contacto que deseas actualizar: ")
   numero = input("Nuevo número de éste contacto: ")
   agenda_telefonica[nombre] = numero
   imprimir_operacion("Contacto Actualizado")


def ver_contacto():
    nombre = input("Nombre del contacto: ")
    nombre_operacion = None
    try:
        nombre_operacion = nombre + " - " + agenda_telefonica[nombre]
    except KeyError:
        nombre_operacion = "Ese contacto no existe"
   
    imprimir_operacion(nombre_operacion)


def ver_todo():
    nombre_operacion = None 
    if len(agenda_telefonica) ==0:
        nombre_operacion = "No tienes ningún contacto"
    else:
        for contacto in agenda_telefonica:
            if nombre_operacion == None: 
                nombre_operacion = "{} - {}".format(contacto,agenda_telefonica[contacto])
            else:
                nombre_operacion += "\n{} - {}".format(contacto,agenda_telefonica[contacto])
            print(contacto + "-" + agenda_telefonica[contacto])
    imprimir_operacion(nombre_operacion)
def iniciar_agenda():
    print("Bienvenido a la agenda telefónica de Luis")
    while True:
        print("1.- Agregar Contacto")
        print("2.- Remover Contacto")
        print("3.- Actualizar Contactos")
        print("4.- Ver un contacto")
        print("5.- Ver todos los contactos")
        print("6.- Salir")
        try:
            operacion = int(input(": "))
        except ValueError:
            print()
            print("Por favor selecciona un número del 1 al 6")
            print()
        else:
            if operacion == 1:
                agregar_contacto()
            elif operacion == 2:
                remover_contacto()
            elif operacion == 3:
                actualizar_contacto()
            elif operacion == 4:
                ver_contacto()
            elif operacion == 5:
                ver_todo()
            elif operacion == 6:
                break
            else:
                print("Operación desconocida")

def despedida():
    print()
    print("--------Gracias por usar nuestra agenda telefónica---------")
    print()

iniciar_agenda()
despedida()