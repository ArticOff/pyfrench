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

from pyfrench import couleur, terminal, logique, maths, aléatoire, retour

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
    return print(str(texte) + couleur.FIN)
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
    return input('{}\n{}: '.format(question, nom) + couleur.FIN)

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
    return f'https://www.google.com/search?q={resutlat.replace(" ", "+")}'
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
    return f'https://www.youtube.com/watch?v={recherche}'