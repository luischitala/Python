from player import Player



sorcerer = Player(40,80,"Sorcerer","Ice barrage")


print("El sorcerer tiene: ")
print(sorcerer.hit_points)
print(sorcerer.mana)
print(sorcerer.vocation)
print(sorcerer.lanzar_hechizo())

knight = Player(80,20,"Knight")


print("El knight tiene:")
print(knight.hit_points)
print(knight.mana)
print(knight.vocation)
print(knight.lanzar_hechizo())

#paladin 
#druid

paladin = Player(70,50,"Paladin","Blessed cross")
print("El knight tiene:")
print(paladin.hit_points)
print(paladin.mana)
print(paladin.vocation)
print(paladin.lanzar_hechizo())

druid = Player(50,70,"Druid","Fire wave")
print("El knight tiene:")
print(druid.hit_points)
print(druid.mana)
print(druid.vocation)
print(druid.lanzar_hechizo())
