import pyxel
from random import *

def contact_mousse (btn,etat_jeu):#les btn n'ont pas la meme taille différement l'etat ou le bouton
    if btn == "doc" :
        if etat_jeu == -1 :
            if contact(112,30,32) : # x / y / size
                if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) : # on relache la souris sur le btn
                    return True
        elif etat_jeu == 2 :
            if contact(0,21,32) :
                if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) :
                    return True

    elif btn == "set" :
        if etat_jeu == -1 :
            if contact(240,0,16) :
                if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) :
                    return True
        elif etat_jeu == 2 :
            if contact(240,25,16) :
                if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) :
                    return True

    elif btn == "ext" :
        if etat_jeu == -2 :
            if contact(240,0,16) :
                if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) :
                    return True
        elif etat_jeu == -3 :
            if contact(240,240,16) :
                if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) :
                    return True

    elif btn == "run" :
        if etat_jeu == 0 :
            if contact(112,192,32) :
                if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) :
                    return True
        elif etat_jeu == -3 :
            if contact(224,224,32) :
                if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) :
                    return True
    return False

def coord_lettre (X,coord): #X notre letre et coord la coordoné "x" ou "y"
    tab_letr = [["A",0,0],["B",0,16],["C",0,32],["D",0,48],["E",0,64],["F",0,80],["G",0,96],["H",0,112],["I",0,128],["J",0,144],["K",0,160],["L",0,176],["M",0,192],["N",0,208],["O",0,224],["P",0,240],["Q",16,0],["R",16,16],["S",16,32],["T",16,48],["U",16,64],["V",16,80],["W",16,96],["X",16,112],["Y",16,128],["Z",16,144],["SPACE",16,160],["UP",16,176],["DOWN",16,192],["RIGHT",16,128],["LEFT",16,224],["1",32,0],["2",32,16],["3",32,32],["4",32,48],["5",32,64],["6",32,80],["7",32,96]]
    if coord == "x" : #on cherche x
        for el in tab_letr :
            if X == el[0]:
                return el[1]
    elif coord == "y" : #on cherche x
        for el in tab_letr :
            if X == el[0]:
                return el[2]

def contact (x,y,size):
    if x <= pyxel.mouse_x <= x + size  and y <= pyxel.mouse_y <= y + size :
        return True
    return False

def type_alleatoir () :
    proba = randint(0,100)
    if proba < 20 : # 20 % rouge
        return 1
    elif 20 <= proba < 25 : # 5% bleu
        return 2
    elif 25 <= proba < 35 : # 10% vert
        return 3
    elif 35 <= proba < 55 : #20% jaune
        return 4
    elif 55 <= proba < 80 : # 25% ciel
        return 5
    elif 80 <= proba < 90 : # 10% marron
        return 6
    elif proba >= 90 : #10% gris
        return 7
