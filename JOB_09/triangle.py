# Le script va permettre de dessiner un triangle avec des '_', des '\' et des '/'
# Il va y avoir une entrèe pour déterminer la taille du triangle

# On va créer les variables pour les bordures du triangle
left = "/"
right = "\\"
base = "__"

# Puis la variable de la saisie de l'utilisateur
userinput = int(input("Veuillez saisir un nombre pour déterminer la taille du triangle : "))

# La boucle qui va permettre de dessiner le triangle à l'aide des variables "left, right, base"
for i in range(userinput):
    print((userinput - i) * " " + left + ((i * 2) * " ") + right)
    if i == userinput - 1:
        print(left + base * userinput + right)
