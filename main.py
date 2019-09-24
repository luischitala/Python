from player import Player


sorcerer = Player(hit_points=40,mana=80,vocation="Sorcerer",hechizo="Ice barrage")

print("El sorcerer tiene: ")
print(sorcerer.hit_points)
print(sorcerer.mana)
print(sorcerer.vocation)
print(sorcerer.lanzar_hechizo())

knight = Player(hit_points=40,mana=80,vocation="Knight",hechizo="Vengance")

print("El knight tiene:")
print(knight.hit_points)
print(knight.mana)
print(knight.vocation)
print(knight.lanzar_hechizo())

#paladin 
#druid

paladin = Player(hit_points=70,mana=50,vocation="Paladin",hechizo="Blessed cross")
print("El knight tiene:")
print(paladin.hit_points)
print(paladin.mana)
print(paladin.vocation)
print(paladin.lanzar_hechizo())


druid = Player(hit_points=50,mana=70,vocation="Druid",hechizo="Fire wave")
print("El knight tiene:")
print(druid.hit_points)
print(druid.mana)
print(druid.vocation)
print(druid.lanzar_hechizo())
