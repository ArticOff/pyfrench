from os import *
from pyfrench import couleur, afficher

def write(commande: str):
    afficher(couleur.GRAS + couleur.VERT + "[pyfrench]" + couleur.FIN + couleur.GRAS + " -> {}".format(commande) + couleur.FIN)
    return system(commande)