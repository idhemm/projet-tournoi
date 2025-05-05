import csv
import json

#fonction de lecture csv

def lire_csv(chemin_fichier):
    donnees = []
    with open(chemin_fichier, mode='r', encoding='utf-8') as fichier:
        lecteur = csv.DictReader(fichier)
        for ligne in lecteur:
            donnees.append(ligne)
    return donnees

#fonction sauvegarde json

def sauvegarder_json(donnees, chemin_fichier):
  
    with open(chemin_fichier, mode='w', encoding='utf-8') as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=4)


def ecrire_texte(texte, chemin_fichier):
    with open(chemin_fichier, mode='w', encoding='utf-8') as fichier:
        fichier.write(texte)
