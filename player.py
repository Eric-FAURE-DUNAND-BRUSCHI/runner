import pyxel

class Player() :
    def __init__ (self):
        self.vitesse = 0
        self.px = 124
        self.py = 119
        self.isgrounded = True
        self.vies_max = 100
        self.vies = 100
        self.score = 124
        self.coins = 0
        self.régène = 0
        self.nb_saut = 0

    def life (self):
        if pyxel.frame_count % 30 == 0 : #chaque seconde
            if self.vies + self.régène <= self.vies_max :
                self.vies += self.régène
            else :
                self.vies = self.vies_max

    def moov(self, setting, orbes, debug):
        if pyxel.btn(setting.btn_droite) and self.px < 247 :
            self.px += 1 + orbes.ajouteur_vitesse
            self.score += 1 + orbes.ajouteur_vitesse
        if pyxel.btn(setting.btn_gauche) and self.px > 0:
            self.px -= 2 + orbes.ajouteur_vitesse
            self.score -= 2 + orbes.ajouteur_vitesse

        if pyxel.btn(setting.btn_haut) and (self.isgrounded or (orbes.double_saut and self.nb_saut < 2)) and debug.couldown_saut == 0:
            self.vitesse = -6
            self.nb_saut += 1
            debug.couldown_saut = 5
        self.vitesse = min(6 , self.vitesse+0.9)
        self.py += self.vitesse

    def au_sol (self):
        if self.py + 6 > 124:
            self.py = 119
            self.isgrounded = True
            self.nb_saut = 0
            return True
        self.isgrounded = False
