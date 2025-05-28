
class Orbes ():
    def __init__ (self):
        self.heale = 0 #en pv par seconde

        self.inverseur_dgt = 1 # 1 pas d'inversion / -1 l'invertion
        self.reducteur_dgt = 0 # en pourcentage

        self.double_saut = False

        self.ajouteur_vitesse = 0
        self.multiplicateur_vitesse = 0 #en pourcentage

        self.rouge_activable = True
        self.bleu_activable = True
        self.vert_activable = True
        self.jaune_activable = True
        self.ciel_activable = True
        self.marron_activable = True
        self.gris_activable = True

        self.type_actif = 0 #aucun /rouge / bleu / vert/ jaune / ciel / marron / gris

    def controle_orbe_actif (self, debug):
        if debug.tmps_orb_rouge_activation == 0 and debug.tmps_orb_bleu_activation == 0 and debug.tmps_orb_vert_activation == 0 and debug.tmps_orb_jaune_activation == 0 and debug.tmps_orb_ciel_activation == 0 and debug.tmps_orb_marron_activation == 0 and debug.tmps_orb_gris_activation == 0 : #si rien est activé
            self.type_actif = 0



    def activation_rouge (self, debug, player):
        if player.vies < player.vies_max and debug.tmps_orb_rouge_activation > 0:
            player.vies += 1
            if debug.tmps_orb_rouge_activation <= 7 :
                self.type_actif = 0
                debug.tmps_orb_rouge_couldown = 8*30
                self.type_actif = 0


    def activation_bleu (self, debug, player):
        player.score += (player.score // 10)
        debug.tmps_orb_bleu_couldown = (debug.temps // 10)
        self.type_actif = 0


    def activation_vert (self, debug):
        if debug.tmps_orb_vert_activation > 0 :
            self.inverseur_dgt = -1
            if debug.tmps_orb_vert_activation <= 7 :
                self.type_actif = 0
                self.inverseur_dgt = 1
                debug.tmps_orb_vert_couldown = 12*30


    def activation_jaune (self, debug):
        if debug.tmps_orb_jaune_activation > 0 :
            self.ajouteur_vitesse = 3
            if debug.tmps_orb_jaune_activation <= 7 :
                self.type_actif = 0
                self.ajouteur_vitesse = 0
                debug.tmps_orb_jaune_couldown = 8*30


    def activation_ciel (self, debug):
        if debug.tmps_orb_ciel_activation > 0:
            self.double_saut = True
            if debug.tmps_orb_ciel_activation <= 7 :
                self.type_actif = 0
                self.double_saut = False
                debug.tmps_orb_ciel_couldown = 5*30



    def activation_marron (self, debug):
        if debug.tmps_orb_marron_activation > 0:
            if debug.tmps_orb_marron_activation <= 7 :
                self.type_actif = 0
                debug.tmps_orb_ciel_couldown = 5*30

    def activation_gris (self, debug):
        if debug.tmps_orb_gris_activation > 0:
            self.reducteur_dgt = 90
            if debug.tmps_orb_gris_activation <= 7 :
                self.type_actif = 0
                self.reducteur_dgt = 0
                debug.tmps_orb_gris_couldown = 12*30



    def test_activation (self, debug):
        if debug.tmps_orb_rouge_activation == 0 and debug.tmps_orb_bleu_activation == 0 and debug.tmps_orb_vert_activation == 0 and debug.tmps_orb_jaune_activation == 0 and debug.tmps_orb_ciel_activation == 0 and debug.tmps_orb_marron_activation == 0 and debug.tmps_orb_gris_activation == 0 : #si rien est activé
            if debug.tmps_orb_rouge_couldown > 0 or debug.tmps_orb_rouge_activation > 0 :
                self.rouge_activable = False
            elif debug.tmps_orb_rouge_couldown == 0 :
                self.rouge_activable = True

            if debug.tmps_orb_bleu_couldown > 0 or debug.tmps_orb_bleu_activation > 0 :
                self.bleu_activable = False
            elif debug.tmps_orb_bleu_couldown == 0 :
                self.bleu_activable = True

            if debug.tmps_orb_vert_couldown > 0 or debug.tmps_orb_vert_activation > 0 :
                self.vert_activable = False
            elif debug.tmps_orb_vert_couldown == 0 :
                self.vert_activable = True

            if debug.tmps_orb_jaune_couldown > 0 or debug.tmps_orb_jaune_activation > 0 :
                self.jaune_activable = False
            elif debug.tmps_orb_jaune_couldown == 0 :
                self.jaune_activable = True

            if debug.tmps_orb_ciel_couldown > 0  or debug.tmps_orb_ciel_activation > 0:
                self.ciel_activable = False
            elif debug.tmps_orb_ciel_couldown == 0 :
                self.ciel_activable = True

            if debug.tmps_orb_marron_couldown > 0 or debug.tmps_orb_marron_activation > 0 :
                self.marron_activable = False
            elif debug.tmps_orb_marron_couldown == 0 :
                self.marron_activable = True

            if debug.tmps_orb_gris_couldown > 0 or debug.tmps_orb_gris_activation > 0 :
                self.gris_activable = False
            elif debug.tmps_orb_gris_couldown == 0 :
                self.gris_activable = True
        else : #il y'en a un deja activé
            self.rouge_activable = False
            self.bleu_activable = False
            self.vert_activable = False
            self.jaune_activable = False
            self.ciel_activable = False
            self.marron_activable = False
            self.gris_activable = False
