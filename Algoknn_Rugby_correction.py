import csv
import matplotlib.pyplot as plt
from math import sqrt
import operator

NOM_FICHIER_CSV = "JoueursTop14.csv"

def extractionDonnees(nom_fichier):
    f = open(nom_fichier, encoding="utf8")
    lignes = csv.reader(f,delimiter=";")
    tabJoueurs = []
    return [ligne for ligne in lignes][1:]

def extraireEquipe(donnees,nom_equipe):
    return [donnee for donnee in donnees if donnee[0] == nom_equipe]

def representation(nom_equipe,donnees):
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
            plt.plot(int(donnee[5]), int(donnee[6]), marque,label = donnee[3])
    plt.legend()
    plt.show()

def distance(point1,point2):
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

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
