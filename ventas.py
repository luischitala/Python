#Agregar artículos
#Remover artículos
#Ver artículos

lista_articulos = list()
def agregar_articulo():
    print()
    articulo = input("Nombre del artículo a agregar: ")
    lista_articulos.append(articulo.capitalize())
    print("Artículo agregado")
    print()
def remover_articulo():
    print()
    articulo = input("Nombre del articulo a remover: ")
    lista_articulos.remove(articulo.capitalize())
    print("El artículo ha sido removido")
def ver_articulos():
    print()
    print("----------Lista de compras----------")
    for articulo in lista_articulos:
        print(articulo)
    print("-----------------------------------")
    print()

print("Bienvenido a la lista de compras")
print()
while True:
    print("Estas son las operaciones que puedes realizar")
    print("1.- Agregar artículo")
    print("2.- Remover artículo")
    print("3.- Ver los artículos")
    print("4.- Salir")
    operacion = int(input("Ingresa la opción deseada:  "))
    if operacion == 1:
        agregar_articulo()
    elif operacion == 2:
        remover_articulo()
    elif operacion == 3:
        ver_articulos()
    else:
        break
print("")
print("Gracias por usar nuestra lista de compras")
print("Vuelve pronto!")
