from os import *

# Console
class couleur():
    VIOLET = '\033[95m'
    CYAN = '\033[96m'
    CYAN_FONCÉ = '\033[36m'
    BLEU = '\033[94m'
    VERT = '\033[92m'
    JAUNE = '\033[93m'
    ROUGE = '\033[91m'
    BLANC = '\033[37m'
    NOIR = '\033[30m'
    MAGENTA = '\033[35m'
    GRAS = '\033[1m'
    DIM = '\033[2m'
    NORMAL = '\033[22m'
    SOULIGNE = '\033[4m'
    FIN = '\033[0m'
    def depuis_rgb(rouge: int, vert: int, bleu: int, texte: str):
        if rouge >= 256:
            return print('\033[38;2;235;162;52mATTENTION: Utilisez une valeur de couleur RGB en dessous de 255.' + '\033[22m')
        if vert >= 256:
            return print('\033[38;2;235;162;52mATTENTION: Utilisez une valeur de couleur RGB en dessous de 255.' + '\033[22m')
        if bleu >= 256:
            return print('\033[38;2;235;162;52mATTENTION: Utilisez une valeur de couleur RGB en dessous de 255.' + '\033[22m')
        return "\033[38;2;{};{};{}m{}".format(rouge, vert, bleu, texte)
def txt(nombre: str):
    return int(nombre)
def num(nombre: int):
    return str(nombre)
def afficher(texte: str):
    return print(str(texte) + couleur.FIN)
def demander(question: str):
    return input('{}\n'.format(question) + couleur.FIN)
class retour():
    def erreur(erreur: str):
        return print(couleur.depuis_rgb(255, 0, 0, 'ERREUR: {}'.format(erreur)) + couleur.FIN)
    def attention(texte: str):
        return print(couleur.depuis_rgb(235, 192, 52, 'ATTENTION: {}'.format(texte)) + couleur.FIN)
    def succes(texte: str):
        return print(couleur.depuis_rgb(45, 166, 49, 'SUCCÈS: {}'.format(texte)) + couleur.FIN)
    def conseil(texte: str):
        return print(couleur.depuis_rgb(80, 140, 212, 'CONSEIL: {}'.format(texte)) + couleur.FIN)
def commencePar(texte: str, mot: str):
    return texte.startswith(mot)
def finitPar(texte: str, mot: str):
    return texte.endswith(mot)
class terminal():
    def write(commande: str):
        afficher(couleur.GRAS + couleur.VERT + "[pyfrench]" + couleur.FIN + couleur.GRAS + " -> {}".format(commande) + couleur.FIN)
        return system(commande)

# Fichier
def ouvrir(fichier: str):
    return open(file=fichier)

Vrai = True
Faux = False

# Condition
def si(valeur: bool):
    return valeur
def replacePar(texte: str, caractère1: str, caractère2: str):
    return texte.replace(caractère1, caractère2)

# Processeurs logique
def égale(valeur1: int, valeur2: int):
    if valeur1 == valeur2:
        return True
    else:
        return False
def différentDe(valeur1: int, valeur2: int):
    if valeur1 != valeur2:
        return True
    else:
        return False
def plusGrand(valeur1: int, valeur2: int):
    if valeur1 > valeur2:
        return True
    else:
        return False
def plusPetit(valeur1: int, valeur2: int):
    if valeur1 < valeur2:
        return True
    else:
        return False 
def égalePlusGrand(valeur1: int, valeur2: int):
    if valeur1 >= valeur2:
        return True
    else:
        return False
def égalePlusPetit(valeur1: int, valeur2: int):
    if valeur1 <= valeur2:
        return True
    else:
        return False
def AND(A: int, B: int):
    return A & B
def NOT(A: int):
    return ~A+2
def XOR(x: int, y: int):
    return bool((x and not y) or (not x and y))
def NAND(A: int, B: int):
    return NOT(AND(A, B))
def OR(A: int, B: int):
    return A | B
def NOR(A: int, B: int):
    return NOT(OR(A, B))
def XNOR(A: int, B: int):
    return NOT(XOR(A, B))

# Lien
def google(recherche: str):
    return f'https://www.google.com/search?q={recherche.replace(" ", "+")}'
def youtube(recherche: str):
    return f'https://www.youtube.com/watch?v={recherche}'