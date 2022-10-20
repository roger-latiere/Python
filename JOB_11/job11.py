# Créer un programme job11.py qui va parcourir le contenu du fichier "domains.xml"
# Compter le nombre de noms de domaines

with open("/home/rastree/Python/JOB_11/domains.xml") as f:
    contenu = f.read()
    count = contenu.count("domain")
print(count)