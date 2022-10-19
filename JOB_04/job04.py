# Script utilisant la boucle "WHILE"
# L'utilisateur doit rentrer un chiffre pour qu'ensuite on affiche tous les chiffres de 0 à la valeur entrée par l'utilisateur
# On crée la valeur d'entrée de l'utilisateur, étant un entier , on utilise "int"
a = int(input("Tapez un chiffre entier : "))
# On crée la valeur "i" pour amener la boucle While : on doit partir de 0 et aller jusqu'à la valeur égale à "a"
i = 0
while i<=a:
    print (i)
    i=i+1
# Ci-dessus on a incrémenté "i" pour éviter la boucle infinie, en effet avec "While" il faut notifier l'incrémentation à la différencede "For"