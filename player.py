class Player(object):
    vocation = "No vocation"
    spell = "Puff"
    movement_speed = "50"
    
    def __init__(self,**kwargs):
        self.name = input("Elige tu nombre: ")
        self.hit_points = kwargs.get("hit_points",50)
        self.mana = kwargs.get("mana",50)

    def __str__(self):
        return "{} es un {} tiene: {} hitpoints y {} mana, puede lanzar {} y corre a {} por minuto".format(self.name,
                                self.vocation,
                                self.hit_points,self.mana, self.cast_spell(),self.movement_speed)

    def cast_spell(self):
        return self.spell

    
class NPC(object):
    race = "No race"
    spell = "puff"

    def __init__(self,**kwargs):
        self.hit_points = kwargs.get("hit_points",50)
        self.mana = kwargs.get("mana", 10)
    
    def __str__(self):
        return "El {} tiene: {} hitpoints y {} mana, puede lanzar {} y corre a {} por minuto".format(
                                self.race,
                                self.hit_points,
                                self.mana, 
                                self.cast_spell(),self.movement_speed)

    def cast_spell(self):
        return self.spell

class Goblin(NPC):
    race = "Monster"
    movement_speed = "20"


class Sorcerer(Player):
    vocation = "Sorcerer"
    spell = "Ice barrage"
    movement_speed = "20"
    def cast_spell(self):
        return "{} y Exura".format(self.spell)
class Knight(Player):
    vocation = "Knight"
    spell = "Vengance"
    movement_speed = "50"
#métodos funciones dentro de la clases
    #self es la instancia de la clase

class Druid(Player):
    vocation = "Druid"
    spell = "Blood Barrage"
    movement_speed = "20"
class Paladin(Player):
    vocation = "Paladin"
    spell = "Magic Dart"
    movement_speed = "80"
