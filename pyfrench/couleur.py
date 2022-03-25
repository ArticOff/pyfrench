"""
The MIT License (MIT)

Copyright (c) 2022-today Artic

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

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
    """
    ## Permet d'avoir une couleur selon une valeur RGB.
    
    ## Exemple:
    ```python
    from pyfrench import *

    afficher(couleur.depuis_rgb(45, 103, 165) + 'salut' + couleur.FIN)
    ```
    """
    if rouge >= 256:
        return print('\033[38;2;235;162;52mATTENTION: Utilisez une valeur de couleur RGB en dessous de 255.' + FIN)
    if vert >= 256:
        return print('\033[38;2;235;162;52mATTENTION: Utilisez une valeur de couleur RGB en dessous de 255.' + FIN)
    if bleu >= 256:
        return print('\033[38;2;235;162;52mATTENTION: Utilisez une valeur de couleur RGB en dessous de 255.' + FIN)
    return "\033[38;2;{};{};{}m".format(rouge, vert, bleu)
def depuis_hex(couleur: str):
    """
    ## Permet d'avoir une couleur selon une valeur HEX.
    
    ## Exemple:
    ```python
    from pyfrench import *

    afficher(couleur.depuis_hex('#3449eb') + 'salut' + couleur.FIN)
    ```
    """
    h = couleur.lstrip('#')
    rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    rgb_format1 = str(rgb).replace(",", ";")
    rgb_format2 = rgb_format1.replace("(", "")
    rgb_format3 = rgb_format2.replace(")", "")
    rgb_format4 = rgb_format3.replace(" ", "")
    return '\033[38;2;{}m'.format(rgb_format4)