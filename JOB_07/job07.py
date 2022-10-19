# Ce script va parcourir et lister les nombres entiers de 1 à 100.
# Pour les multiples de 3, afficher "Fizz"
# Pour les multiples de 5, afficher "Buzz"
# Pour les multiples de 3 et 5, afficher " FizzBuzz"

# Je vais lister les nombres entiers de 1 à 100
# Je ne me sers pas de la commande "list" car elle empêchera de faire corrrectement l'exercice
# Cela sera "for i in range"
for i in range(1,101):
# J'implémente ensuite une condition avec if/elif/else
# En effet si je suis l'ordre de l'exercice le multiple de 3 et 5 doit être en dernier
# Mais cela va créer un problème car les conditions pour 3 et 5 seront toujours vrai, et la condition de 3 et 5 ne sera pas effectuée
# Ainsi, il faudra placer le code du multiple de 3 et 5 en premier
# Pour sortir le multiple de 3 par exemple : i % 3 == O
# 
    if (i % 3 == 0 and i % 5 == 0):
        print ("FizzBuzz")
    elif (i % 3 == 0):
        print ("Fizz")
    elif (i % 5 == 0):
        print ("Buzz")
    else :
        print (i)

# On peut simplifier le script en créant une variable concernannt le résultat :
#   if (i % 3 == 0 and i % 5 == 0):
#       j = "FizzBuzz"
# .../..
#   else :
#       j = i
#       print (j)
#     