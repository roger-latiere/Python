# Script utilisant la boucle "FOR"
# Deux valeurs doivent être rentrées par l'utilisateur. Il faut afficher uniquement les nombres se trouvant entre la valeur 1 et la valeur 2
# Si les deux valeurs sont égales, on doit afficher "Valeurs égales"
# Annonce de la demande pour entrer les deux valeurs
print ("Entrer deux chiffres entiers")

# Création des deux valeurs d'entrée
n1 = int(input("Valeur 1 : "))
n2 = int(input("Valeur 2 : "))

# La boucle "for i in range" afin de retourner une liste de nombres celon 3 paramètres
# --> (Valeur1+1 car le 1er chiffre ne doit pas être inclus, Valeur2, +1 pour l'incrémantation)
for i in range (n1+1, n2, +1):
    print (i)
# --> "-1" : Afin de pouvoir exécuter le scipt lorsque les valeurs sont inversées, c'est à dire lorsque la valeur 1 est plus élevée que la valeur 2
for i in range (n1-1, n2, -1):
    print (i)
# Lorsque les 2 valeurs entrées sont égales
if n1 == n2:
    print ("Valeurs égales")