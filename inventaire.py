import pyxel

class Inventair ():
    def __init__ (self):
        self.tab_slot = [[None,0],[None,0],[None,0],[None,0],[None,0],[None,0],[None,0]]
        self.slot_actuel = 0

    def moov_inventaire (self, setting):
        self.slot_actuel = (self.slot_actuel + ( - pyxel.mouse_wheel)) % 7
        if pyxel.btn(setting.btn_inventaire0) :
            self.slot_actuel = 0
        elif pyxel.btn(setting.btn_inventaire1) :
            self.slot_actuel = 1
        elif pyxel.btn(setting.btn_inventaire2) :
            self.slot_actuel = 2
        elif pyxel.btn(setting.btn_inventaire3) :
            self.slot_actuel = 3
        elif pyxel.btn(setting.btn_inventaire4) :
            self.slot_actuel = 4
        elif pyxel.btn(setting.btn_inventaire5) :
            self.slot_actuel = 5
        elif pyxel.btn(setting.btn_inventaire6) :
            self.slot_actuel = 6

    def controleur_slot (self):
        for slote in self.tab_slot :
            if slote[1] <= 0 and slote[0] != None :
                slote[0] = None

    def add(self, color: str):
        for slot in self.tab_slot:
            if slot[0] == color:
                slot[0] = color
                slot[1] += 1
                return
        for slot in self.tab_slot:
            if slot[0] == None:
                slot[0] = color
                slot[1] += 1
                return

    def activateur (self, orbes, debug, player, setting):
        if self.tab_slot [self.slot_actuel][0] != None and (pyxel.btn(setting.btn_utlise) or pyxel.btn(pyxel.MOUSE_BUTTON_LEFT)) :
            if self.tab_slot [self.slot_actuel][0] == "rouge" and orbes.rouge_activable :
                orbes.type_actif = 1
                debug.tmps_orb_rouge_activation = 300
                player.vies_max += 5
                self.tab_slot [self.slot_actuel][1] -= 1
                player.loot_rouge -= 1

            elif self.tab_slot [self.slot_actuel][0] == "bleu" and orbes.bleu_activable:
                orbes.type_actif = 2
                orbes.activation_bleu(debug, player)
                self.tab_slot [self.slot_actuel][1] -= 1
                player.loot_bleu -= 1

            elif self.tab_slot [self.slot_actuel][0] == "vert" and orbes.vert_activable:
                orbes.type_actif = 3
                debug.tmps_orb_vert_activation = 150
                self.tab_slot [self.slot_actuel][1] -= 1
                player.loot_vert -= 1

            elif self.tab_slot [self.slot_actuel][0] == "jaune" and orbes.jaune_activable:
                orbes.type_actif = 4
                debug.tmps_orb_jaune_activation = 300
                self.tab_slot [self.slot_actuel][1] -= 1
                player.loot_jaune -= 1

            elif self.tab_slot [self.slot_actuel][0] == "ciel" and orbes.ciel_activable:
                orbes.type_actif = 5
                debug.tmps_orb_ciel_activation = 300
                self.tab_slot [self.slot_actuel][1] -= 1
                player.loot_ciel -= 1

            elif self.tab_slot [self.slot_actuel][0] == "marron" and orbes.marron_activable:
                orbes.type_actif = 6
                debug.tmps_orb_marron_activation = 300
                self.tab_slot [self.slot_actuel][1] -= 1
                player.loot_marron -= 1

            elif self.tab_slot [self.slot_actuel][0] == "gris" and orbes.gris_activable:
                orbes.type_actif = 7
                debug.tmps_orb_gris_activation = 150
                self.tab_slot [self.slot_actuel][1] -= 1
                player.loot_gris -= 1
