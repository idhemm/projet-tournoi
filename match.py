class Match:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.score1 = None
        self.score2 = None

    def definir_scores(self, score1, score2):
        self.score1 = score1
        self.score2 = score2

        if score1 > score2:
            self.joueur1.ajouter_victoire()
        elif score2 > score1:
            self.joueur2.ajouter_victoire()

    def __str__(self):
        if self.score1 is not None and self.score2 is not None:
            return f"{self.joueur1.pseudo} {self.score1} - {self.score2} {self.joueur2.pseudo}"
        else:
            return f"{self.joueur1.pseudo} vs {self.joueur2.pseudo} (non joué)"
