from tournois import Tournoi

def menu():
    print("\n--- Gestionnaire de Tournoi ---")
    print("1. Charger les joueurs")
    print("2. Charger les matchs")
    print("3. Saisir les scores")
    print("4. Afficher le classement")
    print("5. Sauvegarder en JSON")
    print("6. Générer le rapport")
    print("7. Quitter")
    choix = input("Choix : ")
    return choix

def main():
    tournoi = Tournoi("Tournoi Printemps")

    while True:
        choix = menu()

        if choix == "1":
            tournoi.charger_joueurs("data/joueurs.csv")
            print("Joueurs chargés.")
        elif choix == "2":
            tournoi.charger_matchs("data/matchs.csv")
            print("Matchs chargés.")
        elif choix == "3":
            tournoi.saisir_scores()
        elif choix == "4":
            tournoi.afficher_classement()
        elif choix == "5":
            tournoi.sauvegarder_json("data/tournoi.json")
            print("Tournoi sauvegardé dans tournoi.json.")
        elif choix == "6":
            tournoi.generer_rapport("data/rapport.txt")
            print("Rapport généré dans rapport.txt.")
        elif choix == "7":
            print("Fin du programme.")
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
