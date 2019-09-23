from player import Player
print("El jugador tiene:")
print(Player.hit_points)
print(Player.mana)
print(Player.vocation)

sorcerer = Player()
sorcerer.hit_points = 40
sorcerer.mana = 80
sorcerer.vocation = "Sorcerer"

print("El sorcerer tiene: ")
print(sorcerer.hit_points)
print(sorcerer.mana)
print(sorcerer.vocation)

knight = Player()
knight.hit_points = 80
knight.mana = 20
knight.vocation = "Knight"

print("El knight tiene:")
print(knight.hit_points)
print(knight.mana)
print(knight.vocation)