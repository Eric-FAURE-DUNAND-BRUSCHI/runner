import pyxel
from random import *

class Loot ():
    def __init__ (self, ox, oy, type):
        self.ox = ox
        self.oy = oy
        self.type = type #1;2;3;4;5;6;7   0 money 1rouge 2bleu 3vert 4jaune 5ciel 6marron 7gris
        self.size = 8
        self.etat = 0

    def etat_loot (self):
        if self.type == 0 and pyxel.frame_count % 15 == 0: #faire tourner la piéce
            self.etat = (self.etat+1) % 2
        if self.type > 0 and pyxel.frame_count % 10 == 0: #faire grossir/rétrécire
            self.etat = (self.etat+1) % 2

    def moov(self, vecteur):
        self.ox += vecteur
        if self.ox + self.size <= 0 :
            return 4
        return 0
