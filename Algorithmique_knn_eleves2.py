import csv
import matplotlib.pyplot as plt
from math import sqrt
import operator

NOM_FICHIER_CSV = "JoueursTop14.csv"

def extractionDonnees(nom_fichier):
    """
    Cette fonction récupère les données d'un fichier csv et renvoie deux valeurs :
    La liste des descripteurs et la liste de toutes les données
    """
    f = open(nom_fichier, encoding="utf8")
    lignes = csv.reader(f,delimiter=";")
    tabJoueurs = []
    return [...............][1:]

def extraireEquipe(donnees,nom_equipe):
    """
     de l'ensemble des listes, on extrait seulement celles d'une équipe
    Parmi les équipes, on trouve "Agen", "Bayonne", "Bordeaux", "Brive", "Castres", "Clermont",
    "La Rochelle", "Lyon", "Montpellier", "Paris", "Pau", Racing92", "Toulon" et "Toulouse"
    On peut aussi écrire "tous" pour avoir tous les joueurs du top 14
    """
    return [donnee for donnee in donnees if donnee[0] == nom_equipe]

def representation(nom_equipe,donnees):
    """
    data est une liste de joueurs avec leurs caractéristiques.
    On extrait leur taille et poids puis on représente ces données dans un repère
    (une couleur par type de poste la position étant déterminée par la liste des descripteurs)
    Les types de postes sont "Avant", "2ème ligne", "3ème ligne", "Demi", "Trois-Quarts" et "Arrière"
    """
    plt.axis([170, 210, 70, 140])
    plt.ylabel("Poids")
    plt.xlabel("Taille")
    plt.title(nom_equipe)
    labels = []
    for donnee in donnees:
        if donnee[3] == "Avant":
            marque = "bx"
        elif donnee[3] == "2ème ligne":
            marque = "*r"
        elif donnee[3] == "3ème ligne":
            marque = "*g"
        elif donnee[3] == "Demi":
            marque = "^r"
        elif donnee[3] == "Trois-Quarts":
            marque = "*m"
        elif donnee[3] == "Arrière":
            marque = "^b"
        else:
            marque = "^b"
        if donnee[3] in labels:
            plt.plot(int(donnee[5]), int(donnee[6]), marque)
        else:
            labels.append(donnee[3])
            plt.plot(int(donnee[....]), int(donnee....]), marque,label = donnee[.....])
    plt.legend()
    plt.show()

def distance(point1,point2):
    """
    distance euclidienne entre les points de coordonnées (x1;y1) et (x2;y2)
    """
    pass

def classification(k,donnees,taille,poids):
    plus_proches = []
    for donnee in donnees:
        d = distance((int(donnee[5]),int(donnee[6])),(taille,poids))
        plus_proches.append((d,donnee[3]))
    plus_proches =sorted(plus_proches,key= lambda x: x[0],reverse=True)[:k]
    comptages = {}
    for kpp in plus_proches:
        if kpp[1] in comptages.keys():
            comptages[kpp[1]] += 1
        else:
            comptages[kpp[1]] = 1
    comptages = sorted(comptages.items(), key=operator.itemgetter(1), reverse=True)
    return comptages[0][0]




donnees = extractionDonnees(NOM_FICHIER_CSV)
equipe = "Clermont"
donnees_equipe = extraireEquipe(donnees,equipe)

representation(equipe,donnees_equipe)
print(classification(5,donnees,100,120))

for taille in range(160,220,5):
    for poids in range(70,140,5):
        print(taille,poids,classification(5,donnees,taille,poids))
