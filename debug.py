class Debug ():
    def __init__ (self):
        self.time_out_shop = 0
        self.time_pause = 0
        self.temps = 0
        self.couldown_coin = 0
        self.couldown_saut = 0
        self.couldown_loot = 0
        self.game_mode_admine = False

        self.tmps_orb_rouge_activation = 0
        self.tmps_orb_rouge_couldown = 0

        self.tmps_orb_bleu_activation = 0 #inutile instatné
        self.tmps_orb_bleu_couldown = 0

        self.tmps_orb_vert_activation = 0
        self.tmps_orb_vert_couldown = 0

        self.tmps_orb_jaune_activation = 0
        self.tmps_orb_jaune_couldown = 0

        self.tmps_orb_ciel_activation = 0
        self.tmps_orb_ciel_couldown = 0

        self.tmps_orb_marron_activation = 0
        self.tmps_orb_marron_couldown = 0

        self.tmps_orb_gris_activation = 0
        self.tmps_orb_gris_couldown = 0


    def debugs (self):
        if self.time_pause > 0 : #fait redescendre a chaque tic j'usqu'a 0
            self.time_pause -= 1
        elif self.time_pause < 0 : #on sait jamais
            self.time_pause = 0

        if self.time_out_shop > 0 : #fait redescendre a chaque tic j'usqu'a 0
            self.time_out_shop -= 1
        elif self.time_out_shop < 0 : #on sait jamais
            self.time_out_shop = 0

        if self.couldown_coin > 0 : #fait redescendre a chaque tic j'usqu'a 0
            self.couldown_coin -= 1
        elif self.couldown_coin < 0 : #on sait jamais
            self.couldown_coin = 0

        if self.couldown_loot > 0 : #fait redescendre a chaque tic j'usqu'a 0
            self.couldown_loot -= 1
        elif self.couldown_loot < 0 : #on sait jamais
            self.couldown_loot = 0

        if self.couldown_saut > 0:
            self.couldown_saut -= 1

        if self.tmps_orb_rouge_activation > 0 : #fait redescendre a chaque tic j'usqu'a 0
            self.tmps_orb_rouge_activation -= 1
        elif self.tmps_orb_rouge_activation < 0 : #on sait jamais
            self.tmps_orb_rouge_activation = 0

        if self.tmps_orb_rouge_couldown > 0 : #fait redescendre a chaque tic j'usqu'a 0
            self.tmps_orb_rouge_couldown -= 1
        elif self.tmps_orb_rouge_couldown < 0 : #on sait jamais
            self.tmps_orb_rouge_couldown = 0

        if self.tmps_orb_bleu_activation > 0 : #fait redescendre a chaque tic j'usqu'a 0
            self.tmps_orb_bleu_activation -= 1
        elif self.tmps_orb_bleu_activation < 0 : #on sait jamais
            self.tmps_orb_bleu_activation = 0

        if self.tmps_orb_bleu_couldown > 0 : #fait redescendre a chaque tic j'usqu'a 0
            self.tmps_orb_bleu_couldown -= 1
        elif self.tmps_orb_bleu_couldown < 0 : #on sait jamais
            self.tmps_orb_bleu_couldown = 0

        if self.tmps_orb_vert_activation > 0 : #fait redescendre a chaque tic j'usqu'a 0
            self.tmps_orb_vert_activation -= 1
        elif self.tmps_orb_vert_activation < 0 : #on sait jamais
            self.tmps_orb_vert_activation = 0

        if self.tmps_orb_vert_couldown > 0 : #fait redescendre a chaque tic j'usqu'a 0
            self.tmps_orb_vert_couldown -= 1
        elif self.tmps_orb_vert_couldown < 0 : #on sait jamais
            self.tmps_orb_vert_couldown = 0

        if self.tmps_orb_jaune_activation > 0 : #fait redescendre a chaque tic j'usqu'a 0
            self.tmps_orb_jaune_activation -= 1
        elif self.tmps_orb_jaune_activation < 0 : #on sait jamais
            self.tmps_orb_jaune_activation = 0

        if self.tmps_orb_jaune_couldown > 0 : #fait redescendre a chaque tic j'usqu'a 0
            self.tmps_orb_jaune_couldown -= 1
        elif self.tmps_orb_jaune_couldown < 0 : #on sait jamais
            self.tmps_orb_jaune_couldown = 0

        if self.tmps_orb_ciel_activation > 0  : #fait redescendre a chaque seconde j'usqu'a 0
            self.tmps_orb_ciel_activation -= 1
        elif self.tmps_orb_ciel_activation < 0 : #on sait jamais
            self.tmps_orb_ciel_activation = 0

        if self.tmps_orb_ciel_couldown > 0 : #fait redescendre a chaque tic j'usqu'a 0
            self.tmps_orb_ciel_couldown -= 1
        elif self.tmps_orb_ciel_couldown < 0 : #on sait jamais
            self.tmps_orb_ciel_couldown = 0

        if self.tmps_orb_marron_activation > 0 : #fait redescendre a chaque tic j'usqu'a 0
            self.tmps_orb_marron_activation -= 1
        elif self.tmps_orb_marron_activation < 0 : #on sait jamais
            self.tmps_orb_marron_activation = 0

        if self.tmps_orb_marron_couldown > 0 : #fait redescendre a chaque tic j'usqu'a 0
            self.tmps_orb_marron_couldown -= 1
        elif self.tmps_orb_marron_couldown < 0 : #on sait jamais
            self.tmps_orb_marron_couldown = 0

        if self.tmps_orb_gris_activation > 0 : #fait redescendre a chaque tic j'usqu'a 0
            self.tmps_orb_gris_activation -= 1
        elif self.tmps_orb_gris_activation < 0 : #on sait jamais
            self.tmps_orb_gris_activation = 0

        if self.tmps_orb_gris_couldown > 0 : #fait redescendre a chaque tic j'usqu'a 0
            self.tmps_orb_gris_couldown -= 1
        elif self.tmps_orb_gris_couldown < 0 : #on sait jamais
            self.tmps_orb_gris_couldown = 0
