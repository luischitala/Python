
print("Bienvenidos al sistema de inventarios ")

def menu():
    print("1 - Mirar artículos")
    print("2 - Agregar artículos")
    print("3 - Salir")

def opcion():  
    while True:
        operacion = input("Ingresa la opción deseada: ")
        if operacion == "1":
            mirar_articulo()
        elif operacion == "2":
            agregar_articulo(input("Articulo que quieres agregar: "))
        elif operacion == "3":
            break
        else:
            print("Ingrese una opción válida")


def agregar_articulo(articulo):
    archivo_lista = open("lista.txt","a")

    archivo_lista.write("{}\n".format(articulo))
    archivo_lista.close()


def mirar_articulo():
    archivo_lista = open("lista.txt","r")
    contenido = archivo_lista.read()
    archivo_lista.close()
    print(contenido)



menu()
opcion()

