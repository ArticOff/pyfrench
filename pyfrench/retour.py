from pyfrench import afficher, couleur

def erreur(erreur: str):
    return afficher(couleur.depuis_rgb(255, 0, 0) + 'ERREUR: {}'.format(erreur) + couleur.FIN)
def attention(texte: str):
    return afficher(couleur.depuis_rgb(235, 192, 52) + 'ATTENTION: {}'.format(texte) + couleur.FIN)
def succes(texte: str):
    return afficher(couleur.depuis_rgb(45, 166, 49) +  'SUCCÈS: {}'.format(texte) + couleur.FIN)
def conseil(texte: str):
    return afficher(couleur.depuis_rgb(80, 140, 212) + 'CONSEIL: {}'.format(texte) + couleur.FIN)