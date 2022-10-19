# Ce script va demander à l'utilsateur de rentrer un texte
# Par la suite le script devra récupérer ce texte et l'écrire dans un fichier "output.txt"
# Enfin, il faudra récupérer le contenu du fichier "output.txt" et l'afficher dans le terminal

texte = input("Texte : ")
# On crée la variable "fichier" qui se nommera "output.txt" (le 1er parmaètre ou argument de la fonction "open")
# et en 2ème argument on va se donner le droit d'écrire sur ce dossier soit "w"
fichier = open("output.txt", "w")
# Il va falloir écrire le texte a été demandé en input dans output.txt, ainsi la fonction "write"
fichier.write(texte)
# Il va falloir fermet le fichier  sinon cela ne marchera pas, la fonction "close" va permettre de faire cela
fichier.close
# Le programme doit récupérer le contenu et l'afficher dans le terminal
fichier = open("output.txt", "r") # l'arguement "r" pour lire le fichier et pas écrire
print(fichier.read())  # () --> c'est comme une fonction
fichier.close