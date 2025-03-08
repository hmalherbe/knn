import csv
import matplotlib.pyplot as plt

def extractionDonnees(nomFichier):
    """Cette fonction récupère les données d'un fichier csv et renvoie deux valeurs :
    La liste des descripteurs et la liste de toutes les données"""


def extraireEquipe(data,equipe):
    """de l'ensemble des listes, on extrait seulement celles d'une équipe
    Parmi les équipes, on trouve "Agen", "Bayonne", "Bordeaux", "Brive", "Castres", "Clermont",
    "La Rochelle", "Lyon", "Montpellier", "Paris", "Pau", Racing92", "Toulon" et "Toulouse"
    On peut aussi écrire "tous" pour avoir tous les joueurs du top 14"""


def representation(data,descripteurs):
    """data est une liste de joueurs avec leurs caractéristiques.
    On extrait leur taille et poids puis on représente ces données dans un repère
    (une couleur par type de poste la position étant déterminée par la liste des descripteurs)
    Les types de postes sont "Avant", "2ème ligne", "3ème ligne", "Demi", "Trois-Quarts" et "Arrière" """


def distance(x1,y1,x2,y2):
    """distance euclidienne entre les points de coordonnées (x1;y1) et (x2;y2)"""


def rechercheTypePoste(data):
    """dans data, on cherche le type de poste le plus souvent présent (type poste étant d'index 3 dans chaque élément de data)"""



def classification(k,data,taille,poids):
    """une série de données étant fournies, on souhaite extraire la classe type de poste d'un joueur dont la taille et le poids sont fournis
    data est une liste de données de la forme [Equipe, Nom, Poste, Type poste, Date de naissance, Taille, Poids]
    On utilise l'algorithme des k plus proches voisins avec k premier paramètre de cette fonction
    Cet algorithme utilise un tri des données"""


#Deuxième algorithme plus efficace car on ne passe plus par le rangement des valeurs dans l'ordre
def classificationEfficace(k,data,taille,poids):
    """une série de données étant fournies, on souhaite extraire la classe type de poste d'un joueur dont la taille et le poids sont fournis
    data est une liste de données de la forme [Equipe, Nom, Poste, Type poste, Date de naissance, Taille, Poids]
    On utilise l'algorithme des k plus proches voisins avec k premier paramètre de cette fonction
    Cet algorithme ne range pas les données dans l'ordre"""



