# Afficher un prompteur 
# Je crée une variable qui va être définie par l'utilisateur
a = input (">")

# Tant que "a" n'est pas égal à "Au revoir" il y a la boucle "while" et le prompteur s'affiche
while a != "Au revoir":
# La condition si "Bonjour" est écrit, il y a une réponse    
    if a=="Bonjour":
        print ("Bonjour à toi") 
# Pour terminer la condition et ainsi la boucle afin d'éviter tout "bug" dans le script   
    else:    
        print(a)
    a = input (">")
    
