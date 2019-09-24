class Player:
    #métodos funciones dentro de la clases
    #self es la instancia de la clase
    
    def __init__(self,hit_points=50,mana=50,vocation="No vocation",hechizo="Puff"):
        self.hit_points = hit_points
        self.mana = mana
        self.vocation = vocation
        self.hechizo = hechizo

    def lanzar_hechizo(self):
        return self.hechizo
