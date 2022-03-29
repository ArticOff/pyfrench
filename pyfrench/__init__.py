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

from pyfrench import terminal, logique, maths, aléatoire, retour

Vrai = True
Faux = False

def afficher(texte: str):
    """
    ## Écrit du texte dans le terminal.
    ### C'est un ```print```, mais à ma sauce.

    ## Exemple:
    ```python
    from pyfrench import *

    afficher('Tu es génial(e) <3')
    ```
    """
    return print(str(texte) + '\033[0m')
def demander(question: str, nom: str = None):
    """
    ## Texte écrit posé sous forme de question.
    ### C'est un ```input```, mais à ma sauce (pas trop piquant ?)

    ## Exemple:
    ```python
    from pyfrench import *

    demander("Qu\'avez-vous mangé à midi ?")
    ```
    """
    if nom == None:
        nom = 'Vous'
    return input('{}\n{}: '.format(question, nom) + '\033[0m')

# Condition
def si(valeur: bool):
    """
    ## Renvoie une valeur booléenne.

    ## Exemple:
    ```python
    from pyfrench import *

    je_suis_faux = False
    afficher(si(je_suis_faux))
    ```
    """
    return valeur
def replacePar(texte: str, caractère1: str, caractère2: str):
    """
    ## Remplace un caractère par un autre dans un texte.

    ## Exemple:
    ```python
    from pyfrench import *

    ma_phrase_stylé = 'coucou, comment ça va car moi, je vais supééééér bien.'
    afficher(replacePar(ma_phrase_stylé, ' ', '-'))
    ```
    """
    return texte.replace(caractère1, caractère2)

def commencePar(texte: str, mot: str):
    """
    ## Renvoie une valeur boolénne si un texte commence par un certain mot.

    ## Exemple:
    ```python
    from pyfrench import *

    ma_phrase_stylé = 'coucou, comment ça va car moi, je vais supééééér bien.'
    afficher(commencePar(ma_phrase_stylé, 'coucou'))
    ```
    """
    return texte.startswith(mot)
def finitPar(texte: str, mot: str):
    """
    ## Renvoie une valeur boolénne si un texte finit par un certain mot.

    ## Exemple:
    ```python
    from pyfrench import *

    ma_phrase_stylé = 'coucou, comment ça va car moi, je vais supééééér bien.'
    afficher(commencePar(ma_phrase_stylé, '.'))
    ```
    """
    return texte.endswith(mot)

# Fichier
def ouvrir(fichier: str):
    """
    ## Ouvre un ficher
    ### C'est tout.

    ## Exemple:
    ```python
    from pyfrench import *

    ouvrir('driver.dll')
    ```
    ### Ne le faites pas, c'est juste un *exemple*. Faites le sur les pc du cdi, c'est mieux xD
    """
    return open(file=fichier)

# Lien
def google(recherche: str):
    """
    ## Effectue une recherche Google.

    ## Exemple:
    ```python
    from pyfrench import *

    afficher(google('je suis bô'))
    ```
    """
    resutlat = recherche.replace("+", "%2B")
    return 'https://www.google.com/search?q={}'.format(resutlat.replace(" ", "+"))
def youtube(recherche: str):
    """
    ## Effectue une recherche YouTube.

    ## Exemple:
    ```python
    from pyfrench import *

    afficher(youtube('fPO76Jlnz6c'))
    ```
    ### Musique de légende !!!
    """
    return 'https://www.youtube.com/watch?v={}'.format(recherche)

# Couleur
class Couleur:
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
            return print('\033[38;2;235;162;52mATTENTION: Utilisez une valeur de couleur RGB en dessous de 255.' + Couleur.FIN)
        if vert >= 256:
            return print('\033[38;2;235;162;52mATTENTION: Utilisez une valeur de couleur RGB en dessous de 255.' + Couleur.FIN)
        if bleu >= 256:
            return print('\033[38;2;235;162;52mATTENTION: Utilisez une valeur de couleur RGB en dessous de 255.' + Couleur.FIN)
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

couleur = Couleur