import re

archivo = open("sample.txt",encoding="utf-8")

informacion = archivo.read()
archivo.close()

print(informacion)

print(re.search(r"GODOT",informacion))