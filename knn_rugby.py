import csv

## Lecture du fichier csv
## et stockage dans une liste de liste
## taille, le poids et le poste si non vide
joueurs = []
with open('./joueurs-top14.csv', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    # Itération sur les lignes
    for ligne in reader:
        taille = ligne["taille(cm)"]
        poids = ligne["poids(kg)"]
        poste = ligne["poste"]
        if taille and poids and poste:
            joueurs.append([int(taille), int(poids), poste])

print("Nbre de joueurs:", len(joueurs))
print("Premier joueur:", joueurs[0])
print("Quatrième joueur:", joueurs[3])

postes = []
for joueur in joueurs:
    poste = joueur["poste"]
    if poste not in postes:
        ...
        
## tests
assert len(postes) == 10
print("Si on choisissait au hasard on aurait une chance sur 10")
print("Soit 90% d'erreurs")
assert postes == ['Demi mêlée',
 'Arrière',
 '1ère ligne',
 'Centre',
 'Ailier',
 '3e ligne',
 'Trois quart aile',
 'Trois quart centre',
 "Demi d'ouverture",
 '2e ligne']