def checar_entrada(edad):
    if edad < 18:
        print("No puedes entrar")
    elif edad >= 21:
        print("Puedes entrar y puedes beber")
    else:
        print("Puedes entrar pero no puedes beber")

edad = 18

checar_entrada(edad)