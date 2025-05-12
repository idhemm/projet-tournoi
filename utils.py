import csv
import json

def lire_csv(chemin_fichier):
    donnees = []
    try:
        with open(chemin_fichier, mode='r', encoding='utf-8') as fichier:
            lecteur = csv.DictReader(fichier)
            for ligne in lecteur:
                donnees.append(ligne)
    except FileNotFoundError:
        print(f"Fichier introuvable : {chemin_fichier}")
    except Exception as e:
        print(f"Erreur lors de la lecture du CSV : {e}")
    return donnees

def sauvegarder_json(donnees, chemin_fichier):
    """
    Sauvegarde les données (liste ou dictionnaire) dans un fichier JSON.
    """
    try:
        with open(chemin_fichier, mode='w', encoding='utf-8') as fichier:
            json.dump(donnees, fichier, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Erreur lors de la sauvegarde JSON : {e}")

def ecrire_texte(texte, chemin_fichier):

    try:
        with open(chemin_fichier, mode='w', encoding='utf-8') as fichier:
            fichier.write(texte)
    except Exception as e:
        print(f"Erreur lors de l'écriture du texte : {e}")
