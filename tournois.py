from joueurs import Joueur
from match import Match
from utils import lire_csv, sauvegarder_json, ecrire_texte

class Tournoi:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []
        self.matchs = []

    def charger_joueurs(self, chemin_fichier):
        donnees = lire_csv(chemin_fichier)
        for ligne in donnees:
            pseudo = ligne['pseudo']
            victoires = int(ligne.get('victoires', 0))
            joueur = Joueur(pseudo, victoires)
            self.joueurs.append(joueur)

    def trouver_joueur(self, pseudo):
        for joueur in self.joueurs:
            if joueur.pseudo == pseudo:
                return joueur
        return None

    def charger_matchs(self, chemin_fichier):
        donnees = lire_csv(chemin_fichier)
        for ligne in donnees:
            pseudo1 = ligne['joueur1']
            pseudo2 = ligne['joueur2']
            joueur1 = self.trouver_joueur(pseudo1)
            joueur2 = self.trouver_joueur(pseudo2)
            if joueur1 and joueur2:
                match = Match(joueur1, joueur2)
                self.matchs.append(match)

    def saisir_scores(self):
        for match in self.matchs:
            print(f"\nMatch : {match.joueur1.pseudo} vs {match.joueur2.pseudo}")
            try:
                score1 = int(input(f"Score de {match.joueur1.pseudo} : "))
                score2 = int(input(f"Score de {match.joueur2.pseudo} : "))
                match.definir_scores(score1, score2)
            except ValueError:
                print("Entrée invalide. Ce match sera ignoré.")

    def afficher_classement(self):
        classement = sorted(self.joueurs, key=lambda j: j.victoires, reverse=True)
        print("\nClassement final :")
        for i, joueur in enumerate(classement, 1):
            print(f"{i}. {joueur.pseudo} - {joueur.victoires} victoires")

    def sauvegarder_json(self, chemin_fichier):
        tournoi_dict = {
            "nom": self.nom,
            "joueurs": [
                {"pseudo": joueur.pseudo, "victoires": joueur.victoires}
                for joueur in self.joueurs
            ]
        }
        sauvegarder_json(tournoi_dict, chemin_fichier)

    def generer_rapport(self, chemin_fichier):
        rapport = f"Rapport du tournoi : {self.nom}\n"
        rapport += "=" * 30 + "\n\n"

        rapport += "Matchs joués :\n"
        for match in self.matchs:
            rapport += str(match) + "\n"

        rapport += "\nClassement final :\n"
        classement = sorted(self.joueurs, key=lambda j: j.victoires, reverse=True)
        for i, joueur in enumerate(classement, 1):
            rapport += f"{i}. {joueur.pseudo} - {joueur.victoires} victoires\n"

        ecrire_texte(rapport, chemin_fichier)
