from pyfrench import *

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
def depuis_rgb(rouge: int, vert: int, bleu: int):
    if rouge >= 256:
        return afficher('\033[38;2;235;162;52mATTENTION: Utilisez une valeur de couleur RGB en dessous de 255.' + FIN)
    if vert >= 256:
        return afficher('\033[38;2;235;162;52mATTENTION: Utilisez une valeur de couleur RGB en dessous de 255.' + FIN)
    if bleu >= 256:
        return afficher('\033[38;2;235;162;52mATTENTION: Utilisez une valeur de couleur RGB en dessous de 255.' + FIN)
    return "\033[38;2;{};{};{}m".format(rouge, vert, bleu)
def depuis_hex(couleur: str):
    h = couleur.lstrip('#')
    rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    rgb_format1 = str(rgb).replace(",", ";")
    rgb_format2 = rgb_format1.replace("(", "")
    rgb_format3 = rgb_format2.replace(")", "")
    rgb_format4 = rgb_format3.replace(" ", "")
    return '\033[38;2;{}m'.format(rgb_format4)