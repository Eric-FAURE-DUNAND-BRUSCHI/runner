import pyxel

class Tire() :
    def __init__ (self, tx, ty, type, size):
        self.tx = tx
        self.ty = ty
        self.type = type
        self.size = size
        self.etat = 0

    def moov(self, vecteur: int):
        if self.type == 1:
            if self.ty > -8:
                self.ty -= 2.75
            else:
                return 4
        elif self.type == 2:
            if self.ty > -8:
                self.ty -= 1.5
            else:
                return 4
        elif self.type == 3:
            if self.tx > -16:
                self.tx -= 5
            else:
                return 4
        self.tx += vecteur
        return 0
