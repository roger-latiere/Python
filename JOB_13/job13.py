# Créer un script job13.py qui demande à l'utilisateur de renseigner un nombre entier.
# Il faudra parcourir le contenu du fichier "data.txt"
# et compter le nombres de mots ayant le nombre de lettres indiqué par l'utilisateur

nombre = int(input("Entrez un nombre entier : "))

with open("/home/rastree/Python/JOB_13/data.txt","r") as f:
    texte = f.read()
    liste = texte.split()
resultat = 0

for element in liste:
    if len(element) == nombre:
        resultat = resultat + 1

# Afficher le résultat
print("Il y a " + str(resultat) + " mot(s) avec " + str(nombre) + " lettre(s)")  
