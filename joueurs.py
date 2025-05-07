class Joueur:
    def __init__(self, pseudo, victoires=0):
        self.pseudo = pseudo
        self.victoires = victoires

    def ajouter_victoire(self):
        self.victoires += 1

    def __str__(self):
        return f"{self.pseudo} - Victoires : {self.victoires}"
