# Script pour connaitre l'âge de l'utilisateur afin de dire si il est mineur ou majeur
# Afficher la question pour connaitre l'âge
print ("Bonjour, quel âge as-tu ?")
# Demander à l'utilsateur de taper son âge
age = int(input("Tape ton age : "))
#On amméne la condition pour savoir si majeur ou mineur
if(age >= 18):
    print("Tu es majeur")
else:
    print("Tu es mineur")