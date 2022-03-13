from math import *

def calcul(calcul: str):
    return print(int(eval(calcul)))

def nombreNonDuplique(liste: list):
    resultat = 0
    for e in liste:
        resultat ^= e
    return resultat