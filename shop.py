class Shop:
    def __init__ (self):
        self.fibonaci = [1,1]
        #tableau d'augmentation des prix en fonction de l'objet
        # 1 : le soin /2: la régène
        self.nb_achat_vie = 0
        self.nb_achat_regene = 0
        self.prix_vie_init = 10 #initial
        self.prix_vie = 0
        self.quantite_du_heal = 10 #valleur de base
        self.prix_regene_init = 15 #initial
        self.prix_regene = 0
        self.quantite_de_regene = 0.5 #valleur de base

    def fibo (self,n):
        if len(self.fibonaci) == n : #n pas dans le tableau mais prochain element
            self.fibonaci.append(self.fibonaci[n-2] + self.fibonaci[n-1])
            return self.fibonaci[n]
        elif len(self.fibonaci) >= n : #n dans le tableau
            return self.fibonaci[n]
        else : #n ors du tableau
            self.fibonaci.append(self.fibo(n-2) + self.fibo(n-1))
            return self.fibonaci[n]
