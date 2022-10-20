# Créer un programme "job12.py" qui va parcourir le fichier "data.txt"
# Il faudra compter le nombre de mots sans caractères spéciaux qui s'y trouvent.

# Importer le module regex
import re

# Ouvrir le fichier data.txt et le lire
with open("/home/rastree/Python/JOB_12/data.txt") as f:
    texte = f.read()    
# Définir le paramètre de recherche "caractères alphabétiques"
    parametre = "[a-zA-Z]+"
# définir la variable "résult" pour afficher le résultat avec une fonction Regex "re.findall" et son parametre
result = len(re.findall(parametre, texte))
print("Il y a " + str(result) + " mots.")
