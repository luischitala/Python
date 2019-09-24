class Player:
    #métodos funciones dentro de la clases
    #self es la instancia de la clase
    
    def __init__(self,**kwargs):
        self.hit_points = kwargs.get("hit_points",50)
        self.mana = kwargs.get("mana",50)
        self.vocation = kwargs.get("vocation","No vocation")
        self.hechizo = kwargs.get("hechizo","Puff")

    def lanzar_hechizo(self):
        return self.hechizo
