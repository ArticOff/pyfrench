from pyfrench import couleur

Vrai = True
Faux = False

def afficher(texte: str):
    return print(str(texte) + couleur.FIN)
def demander(question: str, nom: str = None):
    if nom == None:
        nom = 'Vous'
    return input('{}\n{}: '.format(question, nom) + couleur.FIN)

# Condition
def si(valeur: bool):
    return valeur
def replacePar(texte: str, caractère1: str, caractère2: str):
    return texte.replace(caractère1, caractère2)

def commencePar(texte: str, mot: str):
    return texte.startswith(mot)
def finitPar(texte: str, mot: str):
    return texte.endswith(mot)

# Fichier
def ouvrir(fichier: str):
    return open(file=fichier)

# Lien
def google(recherche: str): 
    resutlat = recherche.replace("+", "%2B")
    return f'https://www.google.com/search?q={resutlat.replace(" ", "+")}'
def youtube(recherche: str):
    return f'https://www.youtube.com/watch?v={recherche}'