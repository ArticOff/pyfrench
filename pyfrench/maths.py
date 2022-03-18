from math import *
from pyfrench import retour

def calcul(calcul: str):
    return print(int(eval(calcul)))
def nombreNonDuplique(liste: list):
    resultat = 0
    for e in liste:
        resultat ^= e
    return resultat
def txt(nombre: str):
    return int(nombre)
def num(nombre: int):
    return str(nombre)
def Pi(décimal: int = 2):
    if décimal > 48:
        retour.attention('Utilisez un valeur \'décimal\' en dessous de 49')
    return format(pi, '.{}f'.format(décimal))