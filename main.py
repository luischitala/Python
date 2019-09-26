import player

#el metodo antiguo
sorcerer = player.Sorcerer(hit_points=40,mana=80)
print("El sorcerer tiene: ")
print(sorcerer.hit_points)
print(sorcerer.mana)
print(sorcerer.vocation)
print(sorcerer.cast_spell())
print(sorcerer.movement_speed)

knight = player.Knight(hit_points=40,mana=80)

print("El knight tiene:")
print(knight.hit_points)
print(knight.mana)
print(knight.vocation)
print(knight.cast_spell())
print(knight.movement_speed)
 #paladin 
 #druid

paladin = player.Paladin(hit_points=70,mana=50,vocation="Paladin",spell="Blessed cross")

print("El {} tiene: {} hitpoints y {} mana, puede lanzar {} y corre a {}".format(paladin.vocation,
                                paladin.hit_points,paladin.mana, paladin.cast_spell(),paladin.movement_speed))

druid = player.Druid(hit_points = 50,mana = 70,vocation="Druid",spell="Fire wave")
print("El {} tiene: {} hitpoints y {} mana, puede lanzar {} y corre a {}".format(druid.vocation,druid.hit_points,druid.mana, druid.cast_spell(),druid.movement_speed))

