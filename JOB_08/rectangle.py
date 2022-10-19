# Le script va permettre de dessiner un rectangle.
# Il faudra rentrer 2 valeurs : la largeur puis la hauteur
row = int(input("Entrer la largeur :"))
col = int(input("Entrer la longueur :"))

# Attribution d'une valeur dans une variable, pour L et H qui sont dépendants l'un de l'autre
for L in range(row):
    for H in range(col):
# On implémente la condition afin de déterminer l'écriture sur les bords du tableau, pour former le rectangle
# La fonction "end" permet le retour à la ligne de l'impression
        if L==0 or L==(row-1):
            print("-",end="")
        elif H==0 or H==(col-1):
            print("|",end="")
        else :
            print(" ",end="") 
    print()