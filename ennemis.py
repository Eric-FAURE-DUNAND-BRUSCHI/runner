class Ennemi ():
    def __init__ (self, ex: int, ey: int, type: list[2]):
        self.ex = ex
        self.ey = ey
        self.size = 16
        #categorie 0 gris / 1 bleu /2 rouge /3 vert
        self.type = type #cathegorie , skin
        self.etat = 0

    def moov (self, vecteur):
        if self.type[0] == 0:
            if self.ey < 112: self.ey += 0.5
            else: return 4
        elif self.type[0] == 1:
            if self.etat == 0 :
                if self.ey > 208 :
                    self.ey -= 1
                else:
                    self.etat = 1
            elif self.etat == 1 :
                if self.ey < 256 :
                    self.ey += 1
                else:
                    self.etat = 2
            else: return 4
        elif self.type[0] == 2:
            if self.etat == 0 :
                if self.ey > 208 :
                    self.ey -= 1
                else:
                    self.etat = 1
            elif self.etat == 1 :
                if self.ey < 256 :
                    self.ey += 1
                else:
                    self.etat = 2
            else : return 4
        elif self.type[0] == 3:
            if self.etat == 0 :
                if self.ex > 235 :
                    self.ex -= 1
                else:
                    self.etat = 1
            elif self.etat == 1 or self.etat == 2 : #continu de reculé aprés le tire
                if self.ex < 256 :
                    self.ex += 2.5
                else:
                    self.etat += 1 # passe a 2
            else : return 4
        self.ex += vecteur
