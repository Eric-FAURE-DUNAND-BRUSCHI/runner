#! /bin/env python3
import pyxel
from math import *
from random import *
import settings as s
import utilities as u
import debug as d
import shoot as shoot
import shop as sp
import player as p
import Orbes as o
import inventaire as i
import ennemis as e
import loot as l
import save as save

debug = d.Debug()
setting = s.Settings()
shop = sp.Shop()
orbes = o.Orbes()
inventair = i.Inventair()
player = p.Player()
class Jeu ():
    def __init__ (self):
        pyxel.init(256,256,title="runner")
        self.x = 0
        self.etat_jeu = -1
        self.etat_avant = -1
        self.page_doc = 1
        self.tab_ennemis = []
        self.tab_shoot = []
        self.tab_loots = []
        self.spawn = 30
        self.ennemis_longue = False
        self.t_min = 15
        self.t_max = 18

        pyxel.load("1.pyxres")
        pyxel.run(self.update, self.draw)

    def compteur (self):
        if pyxel.frame_count % 30 == 0:
            debug.temps += 1
        if player.vies <= 0 :
            self.etat_jeu = 0
        if pyxel.frame_count % 30 == 0:
            self.spawn = (30 - (debug.temps//50))//1
            self.spawn = max(2, self.spawn)
        if player.score // 500 >= 1 and player.score % 200 == 0:
            self.t_min = max(1, self.t_min - 1)
            self.t_max = max(1, self.t_max - 1)

    def defilement (self):
        if pyxel.btn(setting.btn_droite):
            self.x += 3 + orbes.ajouteur_vitesse
            player.score += 3 + orbes.ajouteur_vitesse
        if pyxel.btn(setting.btn_gauche) and self.x >= 5:
            self.x -= 1 + orbes.ajouteur_vitesse
            player.score -= 1 + orbes.ajouteur_vitesse
        if self.x >= (255*8)-256:
            self.x = 0

    def changuer_etat (self):
        if self.etat_jeu == -1:
            pyxel.mouse(True)
        if (self.etat_jeu == -1 ) and (pyxel.btn(setting.btn_setting) or u.contact_mousse("set",-1) )  : #ouvrir les settings
            pyxel.mouse(True)
            self.etat_avant = self.etat_jeu
            self.etat_jeu = -2
        elif ( self.etat_jeu == 2 ) and (pyxel.btn(setting.btn_setting) or u.contact_mousse("set",2) )  : #ouvrir les settings
            pyxel.mouse(True)
            self.etat_avant = self.etat_jeu
            self.etat_jeu = -2
        if self.etat_jeu == -2 and (pyxel.btn(setting.btn_exit) or u.contact_mousse("ext",-2)) and setting.modif_mod == False : #sortir des settings
            pyxel.mouse(False)
            if self.etat_avant == -1 :
                pyxel.mouse(True)
                self.etat_avant = self.etat_jeu
                self.etat_jeu = -1
            else :
                pyxel.mouse(True)
                self.etat_avant = self.etat_jeu
                self.etat_jeu = 2

        if (self.etat_jeu == -1 ) and (pyxel.btn(setting.btn_doc) or u.contact_mousse("doc",-1)) : #ouvrir la doc
            pyxel.mouse(True)
            self.etat_avant = self.etat_jeu
            self.etat_jeu = -3
        if (self.etat_jeu == 2 ) and (pyxel.btn(setting.btn_doc) or u.contact_mousse("doc",2)) : #ouvrir la doc
            pyxel.mouse(True)
            self.etat_avant = self.etat_jeu
            self.etat_jeu = -3
        elif self.etat_jeu == -3 and (pyxel.btn(setting.btn_exit) or u.contact_mousse("ext",-2)) and self.page_doc == 2 :#sortir de la doc vers pause
            pyxel.mouse(True)
            self.etat_avant = self.etat_jeu
            self.etat_jeu = 2

        if self.etat_jeu == 0 and (pyxel.btn(setting.btn_run) or u.contact_mousse("run",0)):
            self.reset()

        if self.etat_jeu == -3 and (pyxel.btn(setting.btn_run) or u.contact_mousse("run",-3)) and self.etat_avant == -1:
            self.reset()

        if self.etat_jeu == 1 and pyxel.btn(setting.btn_pause) and debug.time_pause == 0 : #mettre pause
            pyxel.mouse(True)
            self.etat_avant = self.etat_jeu
            self.etat_jeu = 2
            debug.time_pause = 15
        if self.etat_jeu == 2 and pyxel.btn(setting.btn_pause) and debug.time_pause == 0 : #sortir de pause
            pyxel.mouse(False)
            self.etat_avant = self.etat_jeu
            self.etat_jeu = 1
            debug.time_pause = 15

    def tourne_page (self):
        if self.page_doc == 1 and self.etat_jeu == -3 and pyxel.btn(setting.btn_droite) :
            self.page_doc = 2
        if self.page_doc == 2 and self.etat_jeu == -3 and pyxel.btn(setting.btn_gauche) :
            self.page_doc = 1

    def reset (self):

        self.x =    0
        self.page_doc = 1
        self.tab_loots = []
        self.tab_ennemis = []
        self.tab_shoot = []

        player.vitesse = 0
        player.px = 124
        player.py = 119
        player.isgrounded = True
        player.vies_max = 100
        player.vies = 100
        player.score =124
        player.coins = 0
        player.régène = 0
        player.loot_rouge = 0
        player.loot_bleu = 0
        player.loot_vert = 0
        player.loot_jaune = 0
        player.loot_ciel = 0
        player.loot_marron = 0
        player.loot_gris = 0
        player.nb_saut = 0

        shop.nb_achat_vie = 0
        shop.nb_achat_regene = 0
        shop.prix_vie_init = 10 #initial
        shop.prix_vie = 0
        shop.quantite_du_heal = 10 #valleur de base
        shop.prix_regene_init = 15 #initial
        shop.prix_regene = 0
        shop.quantite_de_regene = 0.5 #valleur de base

        orbes.heale = 0 #en pv par seconde
        orbes.inverseur_dgt = 1
        orbes.reducteur_dgt = 0 # en pourcentage
        orbes.double_saut = False
        orbes.ajouteur_vitesse = 0
        orbes.rouge_activable = True
        orbes.bleu_activable = True
        orbes.vert_activable = True
        orbes.jaune_activable = True
        orbes.ciel_activable = True
        orbes.marron_activable = True
        orbes.gris_activable = True
        orbes.type_actif = 0

        debug.temps = 0
        debug.time_out_shop = 0
        debug.time_pause = 0
        debug.couldown_coin = 0
        debug.couldown_loote = 0
        debug.game_mode_admine = False
        debug.tmps_orb_rouge_activation = 0
        debug.tmps_orb_rouge_couldown = 0
        debug.tmps_orb_bleu_activation = 0 #inutile instatné
        debug.tmps_orb_bleu_couldown = 0
        debug.tmps_orb_vert_activation = 0
        debug.tmps_orb_vert_couldown = 0
        debug.tmps_orb_jaune_activation = 0
        debug.tmps_orb_jaune_couldown = 0
        debug.tmps_orb_ciel_activation = 0
        debug.tmps_orb_ciel_couldown = 0
        debug.tmps_orb_marron_activation = 0
        debug.tmps_orb_marron_couldown = 0
        debug.tmps_orb_gris_activation = 0
        debug.tmps_orb_gris_couldown = 0

        inventair.tab_slot = [[None,0],[None,0],[None,0],[None,0],[None,0],[None,0],[None,0]]
        inventair.slot_actuel = 0

        pyxel.mouse(False)
        self.etat_jeu = 1

    def update(self):
        debug.debugs ()
        game_mode_admin()

        if self.etat_jeu == 2 : #pause/shop
            self.changuer_etat()
            the_shop()

        elif self.etat_jeu == -1 : #ecrant de base
            self.changuer_etat()

        elif self.etat_jeu == -2 : #setting
            setting.defilment()
            setting.reset()
            self.changuer_etat()

            if setting.etape_modif == 1 :
                setting.activateur()

            elif setting.etape_modif == 2 :
                setting.get_touch ()


        elif self.etat_jeu == -3 and self.etat_avant == -1 : #doc au start
            if self.page_doc == 2 :
                self.changuer_etat()
            self.tourne_page()

        elif self.etat_jeu == -3 and self.etat_avant == 2 : #doc en pause
            self.tourne_page()
            self.changuer_etat()

        elif self.etat_jeu == 1 : #in game
            self.changuer_etat()
            self.compteur()
            self.defilement()
            self.moov()
            self.creation_ennemis()
            self.creation_loot()
            self.creation_tire()
            self.contacte_mob()
            self.contacte_loot()
            self.contacte_tir()

            player.moov(setting, orbes, debug)
            player.au_sol()
            player.life()

            for loot in self.tab_loots:
                loot.etat_loot()

            orbes.controle_orbe_actif(debug)
            orbes.test_activation(debug)
            orbes.activation_rouge(debug, player)
            orbes.activation_vert(debug)
            orbes.activation_jaune(debug)
            orbes.activation_ciel(debug)
            orbes.activation_marron(debug)
            orbes.activation_gris(debug)

            inventair.activateur(orbes, debug, player, setting)
            inventair.controleur_slot ()
            inventair.moov_inventaire(setting)

        elif self.etat_jeu == 0 : #mort
            self.changuer_etat()

    def draw (self):
        pyxel.cls(0)

        if self.etat_jeu == 2 :#pause / shop

            #le fond
            pyxel.bltm(0,0,0,( self.x ),0,256,256)
            pyxel.bltm(0,0,1,(orbes.type_actif )*256 ,0,256,256,9)
            pyxel.bltm(0,0,1,0 ,256,256,256, 9)

            # bouton pause
            pyxel.blt(230,3,0,104,184,16,16,5)
            pyxel.text(244,8,f"{setting.KEY_X_to_X(setting.btn_pause)}",15)

            #boutons documentation
            pyxel.blt(0,21,0,72,200,32,32,5)
            pyxel.text(13,34,f"{setting.KEY_X_to_X(setting.btn_doc)}",0)

            #setting in game
            pyxel.blt(240,25,0,72,184,16,16,5)
            pyxel.text(247,41,f"{setting.KEY_X_to_X(setting.btn_setting)}",8)

            #les variables
            pyxel.text(20,5,"time:"f"{debug.temps}",7)
            pyxel.text(20,15,"score:"f"{player.score}",7)
            pyxel.text(20,242,"coins:"f"{player.coins}",7)
            pyxel.text(34,110,"K : 10 instant HP :"f"{shop.prix_vie}",0)
            pyxel.text(34,123,"L :+0.5 regeneration per second:"f"{shop.prix_regene}",0)


            #la vie
            pyxel.rectb(128-(player.vies_max//2), 7, player.vies_max+2, 12, 9)
            pyxel.rect(79, 8, player.vies, 10, 2)


        elif self.etat_jeu == 1: #jeu actif

            #le fond
            pyxel.bltm(0,0,0,( self.x ),0,256,256)

            #les controle pour les 35 première secondes
            if debug.temps <= 35 :
                pyxel.blt(30, 104, 0, 96, 128, 16, 16, 5)
                pyxel.blt(46, 88, 0, 112, 128, 16, 16, 5)
                pyxel.blt(62, 104, 0, 80, 128, 16, 16, 5)


            # le joueur
            if orbes.type_actif == 1: #rouge
                pyxel.blt(player.px, player.py, 0, 20, 59, 9, 9, 9)
            elif orbes.type_actif == 2: #bleu
                pyxel.blt(player.px, player.py, 0, 52, 43, 9, 9, 9)
            elif orbes.type_actif == 3: #vert
                pyxel.blt(player.px, player.py, 0, 36, 43, 9, 9, 9)
            elif orbes.type_actif == 4: #jaune
                pyxel.blt(player.px, player.py, 0, 36, 59, 9, 9, 9)
            elif orbes.type_actif == 5: #ciel
                pyxel.blt(player.px, player.py, 0, 4, 59, 9, 9, 9)
            elif orbes.type_actif == 6: #marron
                pyxel.blt(player.px, player.py, 0, 52, 59, 9, 9, 9)
            elif orbes.type_actif == 7: #gris
                pyxel.blt(player.px, player.py, 0, 20, 43, 9, 9, 9)
            else: #skin de base
                pyxel.blt(player.px, player.py, 0, 4, 43, 9, 9, 9)


            #les entitées
            for mob in self.tab_ennemis :
                if mob.type[0] == 0:
                    pyxel.blt(mob.ex, mob.ey, 0, 0+16*mob.type[1] ,24,mob.size, -mob.size, 5)
                elif mob.type[0] == 1:
                    pyxel.blt(mob.ex, mob.ey, 0, 0 ,8,mob.size, mob.size, 5)
                elif mob.type[0] == 2:
                    pyxel.blt(mob.ex, mob.ey, 0, 16 ,8,mob.size, mob.size, 5)
                elif mob.type[0] == 3:
                    pyxel.blt(mob.ex, mob.ey, 0, 32 ,8,-mob.size, mob.size, 5)

            for shoot in self.tab_shoot:
                print(f'shoot type: {shoot.type}')
                if shoot.type == 1:
                    pyxel.blt(shoot.tx ,shoot.ty,0, 48 ,72,shoot.size, shoot.size, 5)
                elif shoot.type == 2:
                    pyxel.blt(shoot.tx ,shoot.ty,0, 56 ,72,shoot.size, shoot.size, 5)
                elif shoot.type == 3:
                    pyxel.blt(shoot.tx ,shoot.ty,0, 0+(16*shoot.etat) ,104,shoot.size, shoot.size, 5)

            for loot in self.tab_loots:
                if loot.type == 0: #pièce
                    pyxel.blt(loot.ox, loot.oy,0, 32 + (8*loot.etat) ,96, loot.size, loot.size,0)
                elif loot.type == 1 : #rouge
                    pyxel.blt(loot.ox, loot.oy,0, 16 + (8*loot.etat),88, loot.size, loot.size,0)
                elif loot.type == 2 : #bleu
                    pyxel.blt(loot.ox, loot.oy,0, 0 + (8*loot.etat),88, loot.size, loot.size,0)
                elif loot.type == 3 : #vert
                    pyxel.blt(loot.ox, loot.oy,0, 0 + (8*loot.etat),96, loot.size, loot.size,0)
                elif loot.type == 4 : #jaune
                    pyxel.blt(loot.ox, loot.oy,0, 32 + (8*loot.etat),88, loot.size, loot.size,0)
                elif loot.type == 5 : #ciel
                    pyxel.blt(loot.ox, loot.oy,0, 48 + (8*loot.etat),96, loot.size, loot.size,0)
                elif loot.type == 6 : #marron
                    pyxel.blt(loot.ox, loot.oy,0, 48 + (8*loot.etat),88, loot.size, loot.size,0)
                elif loot.type == 7 : #gris
                    pyxel.blt(loot.ox, loot.oy,0, 16 + (8*loot.etat),96, loot.size, loot.size,0)


            #les bordures estetiques
            pyxel.bltm(0,0,1,(orbes.type_actif )*256 ,0,256,256,9)

            # bouton pause
            pyxel.blt(230,3,0,88,184,16,16,5)
            pyxel.text(244,8,f"{setting.KEY_X_to_X(setting.btn_pause)}",15)

            #les varriables
            pyxel.text(20,5,"time:"f"{debug.temps}",7)
            pyxel.text(20,15,"score:"f"{player.score}",7)
            pyxel.rectb(128-(player.vies_max//2), 7, player.vies_max+2, 12, 9)
            pyxel.rect(128-(player.vies_max//2) +1, 8, player.vies, 10, 2)
            pyxel.text(116,10,f"{player.vies}" "/" f"{player.vies_max}", 7 )
            pyxel.text(20,242,"coins:"f"{player.coins}",7)


            #le curseur
            pyxel.blt( 72+ (16*inventair.slot_actuel) ,236,0,240,88,16,16,0)
            #inventair
            x_slot = 72
            for slot in inventair.tab_slot :
                if slot[0] == "rouge":
                    pyxel.blt(x_slot,236,0,160,72,16,16,0)
                    pyxel.text(x_slot+11,245,f"{slot[1]}",0)
                    pyxel.rect(x_slot+1,237, min(debug.tmps_orb_rouge_activation // 14,14),14,2)
                    x_slot += 16
                elif slot[0] == "bleu":
                    pyxel.blt(x_slot,236,0,224,72,16,16,0)
                    pyxel.text(x_slot+11,245,f"{slot[1]}",0)
                    pyxel.rect(x_slot+1,237, min(debug.tmps_orb_bleu_couldown // 14,14),14,2)
                    x_slot += 16
                elif slot[0] == "vert":
                    pyxel.blt(x_slot,236,0,176,72,16,16,0)
                    pyxel.text(x_slot+11,245,f"{slot[1]}",0)
                    pyxel.rect(x_slot+1,237, debug.tmps_orb_vert_couldown // 14,14,2)
                    x_slot += 16
                elif slot[0] == "jaune":
                    pyxel.blt(x_slot,236,0,192,72,16,16,0)
                    pyxel.text(x_slot+11,245,f"{slot[1]}",0)
                    pyxel.rect(x_slot+1,237, min(debug.tmps_orb_jaune_couldown // 14,14),14,2)
                    x_slot += 16
                elif slot[0] == "ciel":
                    pyxel.blt(x_slot,236,0,128,72,16,16,0)
                    pyxel.text(x_slot+11,245,f"{slot[1]}",0)
                    pyxel.rect(x_slot+1,237, min(debug.tmps_orb_ciel_couldown // 14,14),14,2)
                    x_slot += 16
                elif slot[0] == "marron":
                    pyxel.blt(x_slot,236,0,208,72,16,16,0)
                    pyxel.text(x_slot+11,245,f"{slot[1]}",0)
                    pyxel.rect(x_slot+1,237, min(debug.tmps_orb_marron_couldown // 14,14),14,2)
                    x_slot += 16
                elif slot[0] == "gris":
                    pyxel.blt(x_slot,236,0,144,72,16,16,0)
                    pyxel.text(x_slot+11,245,f"{slot[1]}",0)
                    pyxel.rect(x_slot+1,237, min(debug.tmps_orb_gris_couldown // 14,14),14,2)
                    x_slot += 16
                else : # slot vide
                    pyxel.blt(x_slot,236,0,240,72,16,16,0)
                    x_slot += 16

            #indicateur du temps restant avant la finition du spell
            pyxel.rect(205,239, debug.tmps_orb_rouge_activation // 10,10,7)
            pyxel.rect(205,239, debug.tmps_orb_bleu_activation // 10,10,7)
            pyxel.rect(205,239, debug.tmps_orb_vert_activation // 10,10,7)
            pyxel.rect(205,239, debug.tmps_orb_jaune_activation // 10,10,7)
            pyxel.rect(205,239, debug.tmps_orb_ciel_activation // 10,10,7)
            pyxel.rect(205,239, debug.tmps_orb_marron_activation // 10,10,7)
            pyxel.rect(205,239, debug.tmps_orb_gris_activation // 10,10,7)

        elif self.etat_jeu == 0: #game over

            pyxel.bltm(0,0,0,512,256,256,256)

            pyxel.text(110,80,"GAME OVER",0)
            #btn run
            pyxel.blt(112, 187, 0, 64, 152, 32, 32, 5)
            pyxel.text(126,200,f"{setting.KEY_X_to_X(setting.btn_run)}",8)

            pyxel.text(110,100,"time:"f"{debug.temps}",7)
            pyxel.text(34,44,"score:"f"{player.score}",10)
            pyxel.text(180 ,44,"best score:"f"{save.save(player.score)}",10)
            pyxel.text(20,242,"coins:"f"{player.coins}",7)

        elif self.etat_jeu ==  -1 :#ecrant de base

            pyxel.bltm(0,0,0,0,256,256,256)

            #btn setting
            pyxel.blt(240,0,0,72,184,16,16,5)
            pyxel.text(237,5,f"{setting.KEY_X_to_X(setting.btn_setting)}",8)

            #btn doc
            pyxel.blt(112,30,0,72,200,32,32,5)
            pyxel.text(125,43,f"{setting.KEY_X_to_X(setting.btn_doc)}",0)


        elif self.etat_jeu ==  -2 :#setting

            pyxel.bltm(0,0,0,256,256,256,256)
            #btn exit
            pyxel.blt(240,0,0,120,184,16,16,0)
            pyxel.text(247,6,f"{setting.KEY_X_to_X(setting.btn_exit)}",9)

            for el in setting.tab_touche_affiche :
                pyxel.blt(30,setting.get_y_affichage(el[0]),1, u.coord_lettre(setting.KEY_X_to_X(el[2]),"x") + el[3] ,u.coord_lettre(setting.KEY_X_to_X(el[2]),"y"),16,16,9 )
                if el[1] == setting.btn_gauche:
                    pyxel.text(46,setting.get_y_affichage(el[0])+8,"left",8)

                elif el[1] == setting.btn_droite:
                    pyxel.text(46,setting.get_y_affichage(el[0])+8,"right",8)

                elif el[1] == setting.btn_haut:
                    pyxel.text(46,setting.get_y_affichage(el[0])+8,"up",8)

                elif el[1] == setting.btn_utlise:
                    pyxel.text(46,setting.get_y_affichage(el[0])+8,"use , or",8)
                    pyxel.blt(80,setting.get_y_affichage(el[0]),1, 32 ,112,16,16,9 )
                elif el[1] == setting.btn_pause:
                    pyxel.text(46,setting.get_y_affichage(el[0])+8,"pause",8)

                elif el[1] == setting.btn_setting:
                    pyxel.text(46,setting.get_y_affichage(el[0])+8,"setting",8)

                elif el[1] == setting.btn_exit:
                    pyxel.text(46,setting.get_y_affichage(el[0])+8,"exit",8)
                    pyxel.blt(240,0,0,120,184,16,16,0)

                elif el[1] == setting.btn_run:
                    pyxel.text(46,setting.get_y_affichage(el[0])+8,"run the game / play",8)

                elif el[1] == setting.btn_doc:
                    pyxel.text(46,setting.get_y_affichage(el[0])+8,"documentation",8)

                elif el[1] == setting.btn_inventaire0:
                    pyxel.text(46,setting.get_y_affichage(el[0])+8,"slot 1",8)

                elif el[1] == setting.btn_inventaire1:
                    pyxel.text(46,setting.get_y_affichage(el[0])+8,"slot 2",8)

                elif el[1] == setting.btn_inventaire2:
                    pyxel.text(46,setting.get_y_affichage(el[0])+8,"slot 3",8)

                elif el[1] == setting.btn_inventaire3:
                    pyxel.text(46,setting.get_y_affichage(el[0])+8,"slot 4",8)

                elif el[1] == setting.btn_inventaire4:
                    pyxel.text(46,setting.get_y_affichage(el[0])+8,"slot 5",8)

                elif el[1] == setting.btn_inventaire5:
                    pyxel.text(46,setting.get_y_affichage(el[0])+8,"slot 6",8)

                elif el[1] == setting.btn_inventaire6:
                    pyxel.text(46,setting.get_y_affichage(el[0])+8,"slot 7",8)
                    pyxel.text(46,setting.get_y_affichage(el[0]) + 8+16,"or use ",8)
                    pyxel.blt(30,setting.get_y_affichage(el[0]) + 16,1, 32 ,128,16,16,9 )

            if setting.etape_modif == 2 :
                pyxel.blt(104,104,1, 96 ,0,48,48,9 )
                pyxel.text(110,123 ,"enter the \n new key ",0)

        elif self.etat_jeu == -3 : #documentation
            if self.page_doc == 1:
                pyxel.bltm(0,0,0,0,512,256,256)
            elif self.page_doc == 2:
                pyxel.bltm(0,0,0,256,512,256,256)
                if self.etat_avant == 2 :
                    #btn exit
                    pyxel.blt(240,240,0,120,184,16,16,0)
                    pyxel.text(247,247,f"{setting.KEY_X_to_X(setting.btn_exit)}",9)
                elif self.etat_avant == -1 :
                    # btn run
                    pyxel.blt(224, 224, 0, 64, 152, 32, 32, 5)
                    pyxel.text(238,237,f"{setting.KEY_X_to_X(setting.btn_run)}",8)

        if debug.game_mode_admine :
            pyxel.rectb(0, 0, 256, 256, 3)

    def creation_tire (self):
        for mob in self.tab_ennemis:
            if mob.type[0] == 1 :
                if pyxel.frame_count % 30 == 0 :
                    tx = mob.ex + 4
                    ty = mob.ey - mob.size
                    type = mob.type[0]
                    self.tab_shoot.append(shoot.Tire(tx, ty, type, 8))
            elif mob.type[0] == 2 :
                if pyxel.frame_count % 40 == 0 :
                    tx = mob.ex + 4
                    ty = mob.ey - mob.size
                    type = mob.type[0]
                    self.tab_shoot.append(shoot.Tire(tx, ty, type, 8))
            elif mob.type[0] == 3 :
                if mob.etat == 1 :
                    tx = mob.ex - mob.size
                    ty = mob.ey
                    type = mob.type[0]
                    self.tab_shoot.append(shoot.Tire(tx, ty, type, 16))
                    mob.etat += 1

    def creation_ennemis(self):
        if pyxel.frame_count % self.spawn == 0:
            X = randint(0,3)
            if X == 0 : #croiseur gris apparaisent par 2
                type = [0,randint(0,3)]
                ex = randint(128,500)
                ey = -16
                self.tab_ennemis.append(e.Ennemi(ex ,ey ,type))
                self.tab_ennemis.append(e.Ennemi(1.5 * ex ,1.5 * ey ,type))

            elif X == 1 and debug.temps >= 10: # croiseur bleu apparaissent pas avant 10 secondes
                type = [1,0]
                ex = randint(64,304)
                ey = 256
                self.tab_ennemis.append (e.Ennemi(ex ,ey ,type))
            elif X == 2 and debug.temps >= 20:# croiseur rouge apparaissent pas avant 20 secondes
                type = [2,0]
                ex = randint(64,304)
                ey = 256
                self.tab_ennemis.append (e.Ennemi(ex ,ey ,type))

            # croiseur vert apparaissent pas avant 30 secondes
            elif X == 3 and not self.ennemis_longue and debug.temps >= 30:
                self.ennemis_longue = True
                type = [3,0]
                ex = 256
                ey = 112
                self.tab_ennemis.append (e.Ennemi(ex ,ey ,type))

    def creation_loot (self):
        if debug.couldown_coin == 0:
            self.tab_loots.append(l.Loot(256, randint(96,120), 0))
            debug.couldown_coin = randint(2,5) * 30 #couldown entre 2 et 5 secondes(*30 pour les 30 frame par seconde)
        if debug.couldown_loot == 0 and player.score >= 500 :
            print("aug feur")
            self.tab_loots.append(l.Loot(256, randint(96,120), u.type_alleatoir()))
            debug.couldown_loot = randint(self.t_min,self.t_max) * 30 #couldown entre t_min et t_max secondes(*30 pour les 30 frame par seconde)

    def contacte_mob (self):
        for mob in self.tab_ennemis:
            if (
                mob.ex <= player.px + 16
                and mob.ey <= player.py + 16
                and mob.ex + 16 >= player.px
                and mob.ey + 16 >= player.py
            ):
                if mob.type[0] == 0 :
                    player.vies -= (5*(1-(orbes.reducteur_dgt/100))) * orbes.inverseur_dgt
                elif mob.type[0] == 3 :
                    player.vies -= (80*(1-(orbes.reducteur_dgt/100))) * orbes.inverseur_dgt
                    self.ennemis_longue = False
                self.tab_ennemis.remove(mob)

    def contacte_tir(self):
        for tir in self.tab_shoot:
            if tir.type == 1 :
                if (tir.tx  <= player.px + 8
                    and tir.ty <= player.py + 8
                    and tir.tx  + 8 >= player.px
                    and tir.ty + 8 >= player.py):
                    player.vies -= (5*(1-(orbes.reducteur_dgt/100))) * orbes.inverseur_dgt
                    self.tab_shoot.remove(tir)
            elif tir.type== 2:
                if (tir.tx  <= player.px + 8
                    and tir.ty <= player.py + 8
                    and tir.tx  + 8 >= player.px
                    and tir.ty + 8 >= player.py):
                    player.vies -= (10*(1-(orbes.reducteur_dgt/100))) * orbes.inverseur_dgt
                    self.tab_shoot.remove(tir)

            elif tir.type == 3 :
                if (tir.tx +3 <= player.px + 10
                    and tir.ty+4 <= player.py + 3
                    and tir.tx  + 13 >= player.px +1
                    and tir.ty + 7 >= player.py -1):
                    player.vies -= (50*(1-(orbes.reducteur_dgt/100))) * orbes.inverseur_dgt
                    self.tab_shoot.remove(tir)

    def moov(self):
        vecteur = 0
        if pyxel.btn(setting.btn_haut) :
            if player.isgrounded and not orbes.double_saut :
                player.vitesse = -8
            elif player.isgrounded or orbes.double_saut :
                if player.nb_saut < 2 and debug.couldown_saut == 0:
                    player.vitesse = -8
                    player.nb_saut += 1
                    debug.couldown_saut = 5
        player.py += min(6 , player.vitesse+0.9)

        if pyxel.btn(setting.btn_droite): vecteur = (2 + orbes.ajouteur_vitesse) * -1
        elif pyxel.btn(setting.btn_gauche):  vecteur = 1 + orbes.ajouteur_vitesse
        for mob in self.tab_ennemis:
            if mob.moov(vecteur) == 4:
                self.tab_ennemis.remove(mob)
        for shoot in self.tab_shoot:
            if shoot.moov(vecteur) == 4:
                self.tab_shoot.remove(shoot)
        for obj in self.tab_loots:
            if obj.moov(vecteur) == 4:
                self.tab_loots.remove(obj)

    def contacte_loot (self):
        color = [None, "rouge", "bleu", "vert", "jaune", "ciel", "marron", "gris"]
        for loot in self.tab_loots:
            if (loot.ox <= player.px + 8 and loot.oy <= player.py + 8 and loot.ox + 8 >= player.px and loot.oy + 8 >= player.py):
                if (loot.type == 0):
                    player.coins += 5
                else:
                    inventair.add(color[loot.type])
                self.tab_loots.remove(loot)

def game_mode_admin():
    if pyxel.btn(pyxel.KEY_G) and pyxel.btn(pyxel.KEY_A) and  pyxel.btn(pyxel.KEY_M) and pyxel.btn(pyxel.KEY_E) :
        debug.game_mode_admine = True

    if debug.game_mode_admine :
        if pyxel.btn(pyxel.KEY_C) and  pyxel.btn(pyxel.KEY_UP):
            player.coins += 100000
        if pyxel.btn(pyxel.KEY_L) and  pyxel.btn(pyxel.KEY_UP):
            player.régène += 100
        if pyxel.btn(pyxel.KEY_T) and  pyxel.btn(pyxel.KEY_UP):
            debug.temps += 5
        if pyxel.btn(pyxel.KEY_T) and  pyxel.btn(pyxel.KEY_DOWN) and debug.temps > 5:
            debug.temps -= 5
        if pyxel.btn(pyxel.KEY_V) and pyxel.btn(pyxel.KEY_DOWN) :
            player.vies -= 5
        if pyxel.btn(pyxel.KEY_V) and pyxel.btn(pyxel.KEY_UP) :
            player.vies += 5

def the_shop():
    shop.prix_vie = shop.prix_vie_init
    shop.prix_regene = (shop.prix_regene_init * (1+ ( (shop.fibo(shop.nb_achat_regene))/100))) // 1

    if (pyxel.btn(pyxel.KEY_K) and player.coins >= shop.prix_vie and debug.time_out_shop == 0 and player.vies + shop.quantite_du_heal <= player.vies_max):
        player.vies += 10
        shop.nb_achat_vie += 1
        player.coins -= shop.prix_vie
        debug.time_out_shop = 15

    if (pyxel.btn(pyxel.KEY_L) and player.coins >= shop.prix_regene and debug.time_out_shop == 0 ):
        player.régène += 0.5
        shop.nb_achat_regene += 1
        player.coins -= shop.prix_regene
        debug.time_out_shop = 15

Jeu()
