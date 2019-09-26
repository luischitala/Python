import player

#el metodo antiguo
sorcerer = player.Sorcerer(hit_points=40,mana=80)
print(sorcerer)

knight = player.Knight(hit_points=40,mana=80)

print(knight)
 #paladin 
 #druid

paladin = player.Paladin(hit_points=70,mana=50,vocation="Paladin",spell="Blessed cross")

print(paladin)

druid = player.Druid(hit_points = 50,mana = 70,vocation="Druid",spell="Fire wave")
print(druid)

goblin = player.Goblin(hit_points = 20, mana = 10, race = "Goblin")
print(goblin)

