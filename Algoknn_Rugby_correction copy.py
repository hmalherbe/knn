import csv
import matplotlib.pyplot as plt
from math import sqrt
import operator
from random import shuffle

TAUX_ENTRAINEMENT = 0.8
IMC = False

NOM_FICHIER_CSV = "JoueursTop14_V2.csv"

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
        if donnee[2] == "Avant":
            marque = "bx"
        elif donnee[2] == "2ème ligne":
            marque = "*r"
        elif donnee[2] == "3ème ligne":
            marque = "*g"
        elif donnee[2] == "Demi":
            marque = "^r"
        elif donnee[2] == "Trois-Quarts":
            marque = "*m"
        elif donnee[2] == "Arrière":
            marque = "^b"
        else:
            marque = "^b"
        if donnee[2] in labels:
            plt.plot(int(donnee[4]), int(donnee[5]), marque)
        else:
            labels.append(donnee[2])
            plt.plot(int(donnee[4]), int(donnee[5]), marque,label = donnee[3])
    plt.legend()
    plt.show()

def distance(point1,point2,IMC=False):
    if IMC:
        imc1 = int(point1[1])/int(point1[0])/int(point1[0])/10000
        imc2 = int(point2[1])/int(point2[0])/int(point2[0])/10000
        return abs(imc1-imc2)
    return sqrt((int(point1[0]) - int(point2[0]))**2 + (int(point1[1]) - int(point2[1]))**2)

def occurence_max(tab):
    """
    Renvoie la valeur qui a le plus d'occurences dans un tableau
    """
    dico = {k: 0 for k in tab}
    for k in tab:
        dico[k] += 1
    
    maxi, k_max = 0 , 0
    for k, v in dico.items():
        if v > maxi:
            maxi, k_max = v , k
    return k_max


def classification(k,donnees,taille,poids):
    plus_proches = []
    for donnee in donnees:
        d = distance((int(donnee[4]),int(donnee[5])),(taille,poids),IMC=IMC)
        # print(d)
        plus_proches.append((d,donnee[2]))
    plus_proches =sorted(plus_proches,key= lambda x: x[0],reverse=False)
    plus_proches =plus_proches[:k]
    plus_proches = [pp[1] for pp in plus_proches]
    return occurence_max(plus_proches)


def plus_proche(i):
    joueur_test = donnees_test[i]
    j_min = 0
    d_min = distance((joueur_test[4],joueur_test[5]),(donnees_entrainement[0][4],donnees_entrainement[0][5]),IMC=IMC)
    for j in range(len(donnees_entrainement)):
        d = distance((joueur_test[4],joueur_test[5]),(donnees_entrainement[j][4],donnees_entrainement[j][5]),IMC=IMC)
        if d < d_min:
            d_min = d
            j_min = j
    return donnees_entrainement[j_min]


def taux_erreur():
    global difference
    erreur = 0
    for i in range(len(donnees_test)):
        le_plus_proche = plus_proche(i)
        poste_predit = le_plus_proche[2]
        poste_reel = donnees_test[i][2]
        if poste_predit != poste_reel:
            # print(poste_predit,poste_reel)
            erreur = erreur + 1
            difference.append(donnees_test[i][1])
    return erreur/len(donnees_test)


def taux_erreur_knn(k):
    global difference_knn
    erreur = 0
    for i in range(len(donnees_test)):
        taille = int(donnees_test[i][4])
        poids = int(donnees_test[i][5])
        poste_predit = classification(k,donnees_entrainement,taille,poids)
        poste_reel = donnees_test[i][2]
        if poste_predit != poste_reel:
            # print(poste_predit,poste_reel)
            erreur = erreur + 1
            difference_knn.append(donnees_test[i][1])
    return erreur/len(donnees_test)


donnees = extractionDonnees(NOM_FICHIER_CSV)
difference = []
difference_knn = []
# shuffle(donnees)
nb_entrainements = int(len(donnees) * TAUX_ENTRAINEMENT)
donnees_entrainement = donnees[len(donnees)-nb_entrainements:]
donnees_test = donnees[:len(donnees)-nb_entrainements]

print("taux erreur",taux_erreur())

# print(plus_proche(2))

equipe = "Clermont"
donnees_equipe = extraireEquipe(donnees,equipe)

representation(equipe,donnees_equipe)
print(classification(5,donnees_entrainement,100,120))
mini_k = 1
mini_erreur = taux_erreur_knn(1)
for k in range(2,20):
    taux_erreur = taux_erreur_knn(k)
    if taux_erreur < mini_erreur:
        mini_erreur = taux_erreur
        mini_k = k
print(mini_k,mini_erreur)

# print(difference)
# print(difference_knn)
# diff_knn_diff = [d for d in difference_knn if not d in difference]
# print(len(diff_knn_diff),diff_knn_diff)

# for taille in range(160,220,5):
#     for poids in range(70,140,5):
#         print(taille,poids,classification(5,donnees,taille,poids))
