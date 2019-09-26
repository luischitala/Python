class Player(object):
    vocation = "No vocation"
    spell = "Puff"
    movement_speed = "50"
    
    def __init__(self,**kwargs):
        self.hit_points = kwargs.get("hit_points",50)
        self.mana = kwargs.get("mana",50)


    def cast_spell(self):
        return self.spell

class Sorcerer(Player):
    vocation = "Sorcerer"
    spell = "Ice barrage"
    movement_speed = "20"
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
