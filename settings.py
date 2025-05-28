import pyxel
import utilities as u

class Settings ():
    def __init__ (self):
        self.btn_gauche = pyxel.KEY_Q
        self.btn_droite = pyxel.KEY_D
        self.btn_haut = pyxel.KEY_Z
        self.btn_utlise = pyxel.KEY_H

        self.btn_pause = pyxel.KEY_P
        self.btn_setting = pyxel.KEY_O
        self.btn_exit = pyxel.KEY_I
        self.btn_run = pyxel.KEY_R
        self.btn_doc = pyxel.KEY_M

        self.btn_inventaire0 = pyxel.KEY_1
        self.btn_inventaire1 = pyxel.KEY_2
        self.btn_inventaire2 = pyxel.KEY_3
        self.btn_inventaire3 = pyxel.KEY_4
        self.btn_inventaire4 = pyxel.KEY_5
        self.btn_inventaire5 = pyxel.KEY_6
        self.btn_inventaire6 = pyxel.KEY_7

        self.y_affichage = 10
        self.x_affichage = 30

        #position, variable ,touche
        self.tab_touche_affiche = [[1,self.btn_gauche,pyxel.KEY_Q,0],[2,self.btn_droite,pyxel.KEY_D,0],[3,self.btn_haut,pyxel.KEY_Z,0],[4,self.btn_utlise,pyxel.KEY_H,0],[5,self.btn_pause,pyxel.KEY_P,0],[6,self.btn_setting,pyxel.KEY_O,0],[7,self.btn_exit,pyxel.KEY_I,0],[8,self.btn_run,pyxel.KEY_R,0],[9,self.btn_doc,pyxel.KEY_M,0],[10,self.btn_inventaire0,pyxel.KEY_1,0],[11,self.btn_inventaire1,pyxel.KEY_2,0],[12,self.btn_inventaire2,pyxel.KEY_3,0],[13,self.btn_inventaire3,pyxel.KEY_4,0],[14,self.btn_inventaire4,pyxel.KEY_5,0],[15,self.btn_inventaire5,pyxel.KEY_6,0],[16,self.btn_inventaire6,pyxel.KEY_7,0]]

        self.modif_mod = False
        self.etape_modif = 1 #0 rien / 1 en attente d'un contact/ 2 en attente d'une touche /3 chekeur et modification
        self.el = None

        self.dico_touche_utilise = {pyxel.KEY_A:0, pyxel.KEY_B:1, pyxel.KEY_C:2, pyxel.KEY_D:3, pyxel.KEY_E:4,pyxel.KEY_F:5,pyxel.KEY_G:6,pyxel.KEY_H:7,pyxel.KEY_I:8,pyxel.KEY_J:9,pyxel.KEY_K:10,pyxel.KEY_L:11,pyxel.KEY_M:12,pyxel.KEY_N:13,pyxel.KEY_O:14,pyxel.KEY_P:15,pyxel.KEY_Q:16,pyxel.KEY_R:17,pyxel.KEY_S:18,pyxel.KEY_T:19,pyxel.KEY_U:20,pyxel.KEY_V:21,pyxel.KEY_W:22,pyxel.KEY_X:23,pyxel.KEY_Y:24,pyxel.KEY_Z:25,pyxel.KEY_SPACE:26,pyxel.KEY_RIGHT:27,pyxel.KEY_LEFT:28,pyxel.KEY_DOWN:29,pyxel.KEY_UP:30,pyxel.KEY_1:31 ,pyxel.KEY_2:32, pyxel.KEY_3:33, pyxel.KEY_4:34, pyxel.KEY_5:35, pyxel.KEY_6:36, pyxel.KEY_7:37 }

        self.tab_touche_utilise= [[pyxel.KEY_A,None],[pyxel.KEY_B,None],[pyxel.KEY_C,None],[pyxel.KEY_D,self.btn_droite],[pyxel.KEY_E,None],[pyxel.KEY_F,None],[pyxel.KEY_G,None],[pyxel.KEY_H,None],[pyxel.KEY_I,self.btn_exit],[pyxel.KEY_J,None],[pyxel.KEY_K,None],[pyxel.KEY_L,None],[pyxel.KEY_M,self.btn_doc],[pyxel.KEY_N,None],[pyxel.KEY_O,self.btn_setting],[pyxel.KEY_P,self.btn_pause],[pyxel.KEY_Q,self.btn_gauche],[pyxel.KEY_R,self.btn_run],[pyxel.KEY_S,None],[pyxel.KEY_T,None],[pyxel.KEY_U,None],[pyxel.KEY_V,None],[pyxel.KEY_W,None],[pyxel.KEY_X,None],[pyxel.KEY_Y,None],[pyxel.KEY_Z,self.btn_haut],[pyxel.KEY_SPACE,None],[pyxel.KEY_RIGHT,None],[pyxel.KEY_LEFT,None],[pyxel.KEY_DOWN,None],[pyxel.KEY_UP,None],[pyxel.KEY_1, self.btn_inventaire0 ],[pyxel.KEY_2, self.btn_inventaire1 ],[pyxel.KEY_3, self.btn_inventaire2 ],[pyxel.KEY_4, self.btn_inventaire3 ],[pyxel.KEY_5, self.btn_inventaire4 ],[pyxel.KEY_6, self.btn_inventaire5 ],[pyxel.KEY_7, self.btn_inventaire6 ]]


# etape 1
    def activateur (self):
        x = 30
        for el in self.tab_touche_affiche :
            y = self.get_y_affichage(el[0])
            size = 16
            if u.contact(x,y,size) :
                el[3] = 48  #decalage pour l'affichage
                if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) :
                    self.modif_mod = True
                    self.etape_modif = 2
                    self.el= el
            else:
                el[3] = 0


#-------------------------------------------------------------------------------
    def defilment (self):
        self.y_affichage = self.y_affichage + (pyxel.mouse_wheel*2)
        if self.y_affichage < -50 :
            self.y_affichage = -50
        if self.y_affichage > 10 :
            self.y_affichage = 10

    def get_y_affichage (self,i): # i est le numéro d'ordres d'apparition de la touche
        return  self.y_affichage + (i*16)

    def reset (self):
        if not self.modif_mod :
            self.etape_modif = 1

#-------------------------------------------------------------------------------

#etape 2
    def get_touch (self) : #la liste du tableau d'affichage
        if pyxel.btn( pyxel.KEY_A ):
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_A,self.el)

        if pyxel.btn( pyxel.KEY_B) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_B,self.el)

        if pyxel.btn( pyxel.KEY_C) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_C,self.el)

        if pyxel.btn( pyxel.KEY_D) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_D,self.el)

        if pyxel.btn( pyxel.KEY_E) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_E,self.el)

        if pyxel.btn( pyxel.KEY_F) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_F,self.el)

        if pyxel.btn( pyxel.KEY_G) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_G,self.el)

        if pyxel.btn( pyxel.KEY_H) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_H,self.el)

        if pyxel.btn( pyxel.KEY_I) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_I,self.el)

        if pyxel.btn( pyxel.KEY_J ):
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_J,self.el)

        if pyxel.btn( pyxel.KEY_K) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_K,self.el)

        if pyxel.btn( pyxel.KEY_L) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_L,self.el)

        if pyxel.btn( pyxel.KEY_M) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_M,self.el)

        if pyxel.btn( pyxel.KEY_N) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_N,self.el)

        if pyxel.btn( pyxel.KEY_O) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_O,self.el)

        if pyxel.btn( pyxel.KEY_P) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_P,self.el)

        if pyxel.btn( pyxel.KEY_Q) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_Q,self.el)

        if pyxel.btn( pyxel.KEY_R) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_R,self.el)

        if pyxel.btn( pyxel.KEY_S) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_S,self.el)

        if pyxel.btn( pyxel.KEY_T) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_T,self.el)

        if pyxel.btn( pyxel.KEY_U) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_U,self.el)

        if pyxel.btn( pyxel.KEY_V) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_V,self.el)

        if pyxel.btn( pyxel.KEY_W) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_W,self.el)

        if pyxel.btn( pyxel.KEY_X) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_X,self.el)

        if pyxel.btn( pyxel.KEY_Y) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_Y,self.el)

        if pyxel.btn( pyxel.KEY_Z ):
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_Z,self.el)

        if pyxel.btn( pyxel.KEY_SPACE) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_SPACE,self.el)

        if pyxel.btn( pyxel.KEY_UP) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_UP,self.el)

        if pyxel.btn( pyxel.KEY_DOWN) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_DOWN,self.el)

        if pyxel.btn( pyxel.KEY_RIGHT) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_RIGHT,self.el)

        if pyxel.btn( pyxel.KEY_LEFT) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_LEFT,self.el)

        if pyxel.btn( pyxel.KEY_1) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_1,self.el)

        if pyxel.btn( pyxel.KEY_2) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_2,self.el)

        if pyxel.btn( pyxel.KEY_3) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_3,self.el)

        if pyxel.btn(pyxel.KEY_4) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_4,self.el)

        if pyxel.btn( pyxel.KEY_5) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_5,self.el)

        if pyxel.btn(pyxel.KEY_6) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_6,self.el)

        if pyxel.btn(pyxel.KEY_7) :
            self.etape_modif = 3
            self.chekeur(self.el[2],pyxel.KEY_7,self.el)



#etape 3
    def chekeur (self,touche_a_changer, nouvelle_touche, el) :# touche à changer et nouvelle touche sont des indices!!
        t0 = self.dico_touche_utilise[touche_a_changer]
        t1 = self.dico_touche_utilise[nouvelle_touche]
        #on test si la touche est déjà asigné ou si les deux sont les même ou si l'ancienne existe:
        if t0 == t1 and self.modif_mod:
            self.modif_mod = False
        if self.tab_touche_utilise[t0][1] is None and self.modif_mod:
            self.modif_mod = False
        if self.tab_touche_utilise[t1][1] is not None and self.modif_mod :
            self.modif_mod = False
        #on echange les varriable et le tableau
        if self.modif_mod:
            self.changeur_manuel(t0, t1,el )


    def changeur_manuel(self,t0 , t1 ,el ) : #t = indice de la touche dans le tableau / remplace la 0 par la 1
        if self.btn_gauche == self.tab_touche_utilise[t0][0] :
            el[2] = self.tab_touche_utilise[t1][0]
            self.btn_gauche = self.tab_touche_utilise[t1][0]
            self.tab_touche_utilise[t1][1] = self.btn_gauche
            el[1] = self.btn_gauche

        elif self.btn_droite== self.tab_touche_utilise[t0][0]:
            el[2] = self.tab_touche_utilise[t1][0]
            self.btn_droite = self.tab_touche_utilise[t1][0]
            self.tab_touche_utilise[t1][1] = self.btn_droite
            el[1] = self.btn_droite

        elif self.btn_haut== self.tab_touche_utilise[t0][0] :
            el[2] = self.tab_touche_utilise[t1][0]
            self.btn_haut = self.tab_touche_utilise[t1][0]
            self.tab_touche_utilise[t1][1] = self.btn_haut
            el[1] = self.btn_haut

        elif self.btn_setting== self.tab_touche_utilise[t0][0] :
            el[2] = self.tab_touche_utilise[t1][0]
            self.btn_setting = self.tab_touche_utilise[t1][0]
            self.tab_touche_utilise[t1][1] = self.btn_setting
            el[1] = self.btn_setting

        elif self.btn_exit== self.tab_touche_utilise[t0][0] :
            el[2] = self.tab_touche_utilise[t1][0]
            self.btn_exit = self.tab_touche_utilise[t1][0]
            self.tab_touche_utilise[t1][1] = self.btn_exit
            el[1] = self.btn_exit

        elif self.btn_pause== self.tab_touche_utilise[t0][0] :
            el[2] = self.tab_touche_utilise[t1][0]
            self.btn_pause = self.tab_touche_utilise[t1][0]
            self.tab_touche_utilise[t1][1] = self.btn_pause
            el[1] = self.btn_pause

        elif self.btn_run== self.tab_touche_utilise[t0][0] :
            el[2] = self.tab_touche_utilise[t1][0]
            self.btn_run = self.tab_touche_utilise[t1][0]
            self.tab_touche_utilise[t1][1] = self.btn_run
            el[1] = self.btn_run

        elif self.btn_doc== self.tab_touche_utilise[t0][0] :
            el[2] = self.tab_touche_utilise[t1][0]
            self.btn_doc = self.tab_touche_utilise[t1][0]
            self.tab_touche_utilise[t1][1] = self.btn_doc
            el[1] = self.btn_doc

        elif self.btn_inventaire0 == self.tab_touche_utilise[t0][0] :
            el[2] = self.tab_touche_utilise[t1][0]
            self.btn_inventaire0 = self.tab_touche_utilise[t1][0]
            self.tab_touche_utilise[t1][1] = self.btn_inventaire0
            el[1] = self.btn_inventaire0

        elif self.btn_inventaire1== self.tab_touche_utilise[t0][0] :
            el[2] = self.tab_touche_utilise[t1][0]
            self.btn_inventaire1 = self.tab_touche_utilise[t1][0]
            self.tab_touche_utilise[t1][1] = self.btn_inventaire1
            el[1] = self.btn_inventaire1

        elif self.btn_inventaire2== self.tab_touche_utilise[t0][0] :
            el[2] = self.tab_touche_utilise[t1][0]
            self.btn_inventaire2 = self.tab_touche_utilise[t1][0]
            self.tab_touche_utilise[t1][1] = self.btn_inventaire2
            el[1] = self.btn_inventaire2

        elif self.btn_inventaire3== self.tab_touche_utilise[t0][0] :
            el[2] = self.tab_touche_utilise[t1][0]
            self.btn_inventaire3 = self.tab_touche_utilise[t1][0]
            self.tab_touche_utilise[t1][1] = self.btn_inventaire3
            el[1] = self.btn_inventaire3

        elif self.btn_inventaire4== self.tab_touche_utilise[t0][0] :
            el[2] = self.tab_touche_utilise[t1][0]
            self.btn_inventaire4 = self.tab_touche_utilise[t1][0]
            self.tab_touche_utilise[t1][1] = self.btn_inventaire4
            el[1] = self.btn_inventaire4

        elif self.btn_inventaire5== self.tab_touche_utilise[t0][0] :
            el[2] = self.tab_touche_utilise[t1][0]
            self.btn_inventaire5 = self.tab_touche_utilise[t1][0]
            self.tab_touche_utilise[t1][1] = self.btn_inventaire5
            el[1] = self.btn_inventaire6

        elif self.btn_inventaire6== self.tab_touche_utilise[t0][0] :
            el[2] = self.tab_touche_utilise[t1][0]
            self.btn_inventaire6 = self.tab_touche_utilise[t1][0]
            self.tab_touche_utilise[t1][1] = self.btn_inventaire6
            el[1] = self.btn_inventaire6

        elif self.btn_utlise== self.tab_touche_utilise[t0][0] :
            el[2] = self.tab_touche_utilise[t1][0]
            self.btn_utlise = self.tab_touche_utilise[t1][0]
            self.tab_touche_utilise[t1][1] = self.btn_utlise
            el[1] = self.btn_utlise

        self.etape_modif = 1
        self.tab_touche_utilise[t0][1] = None
        self.modif_mod = False


    def KEY_X_to_X (self, key):
        if key == pyxel.KEY_A :
            return "A"
        if key == pyxel.KEY_B :
            return "B"
        if key == pyxel.KEY_C :
            return "C"
        if key == pyxel.KEY_D :
            return "D"
        if key == pyxel.KEY_E :
            return "E"
        if key == pyxel.KEY_F :
            return "F"
        if key == pyxel.KEY_G :
            return "G"
        if key == pyxel.KEY_H :
            return "H"
        if key == pyxel.KEY_I :
            return "I"
        if key == pyxel.KEY_J :
            return "J"
        if key == pyxel.KEY_K :
            return "K"
        if key == pyxel.KEY_L :
            return "L"
        if key == pyxel.KEY_M :
            return "M"
        if key == pyxel.KEY_N :
            return "N"
        if key == pyxel.KEY_O :
            return "O"
        if key == pyxel.KEY_P :
            return "P"
        if key == pyxel.KEY_Q :
            return "Q"
        if key == pyxel.KEY_R :
            return "R"
        if key == pyxel.KEY_S :
            return "S"
        if key == pyxel.KEY_T :
            return "T"
        if key == pyxel.KEY_U :
            return "U"
        if key == pyxel.KEY_V :
            return "V"
        if key == pyxel.KEY_W :
            return "W"
        if key == pyxel.KEY_X :
            return "X"
        if key == pyxel.KEY_Y :
            return "Y"
        if key == pyxel.KEY_Z :
            return "Z"
        if key == pyxel.KEY_SPACE :
            return "SPACE"
        if key == pyxel.KEY_UP :
            return "UP"
        if key == pyxel.KEY_DOWN :
            return "DOWN"
        if key == pyxel.KEY_RIGHT :
            return "RIGHT"
        if key == pyxel.KEY_LEFT :
            return "LEFT"
        if key == pyxel.KEY_1 :
            return "1"
        if key == pyxel.KEY_2 :
            return "2"
        if key == pyxel.KEY_3 :
            return "3"
        if key == pyxel.KEY_4 :
            return "4"
        if key == pyxel.KEY_5 :
            return "5"
        if key == pyxel.KEY_6 :
            return "6"
        if key == pyxel.KEY_7 :
            return "7"
