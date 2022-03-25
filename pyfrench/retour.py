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

from pyfrench import couleur

def erreur(erreur: str):
    """
    ## Fait un message d'erreur.
    
    ## Exemple:
    ```python
    from pyfrench import *

    retour.erreur('Pain au chocolat, pas chocolatine')
    ```
    ### J'ai rien contre vous les gens su sud-ouest, vous êtes les best !!!
    """
    return print(couleur.depuis_rgb(255, 0, 0) + 'ERREUR: {}'.format(erreur) + couleur.FIN)
def attention(texte: str):
    """
    ## Fait un message de prévention.
    
    ## Exemple:
    ```python
    from pyfrench import *

    retour.attention('1+1 = 3, pas 2...')
    """
    return print(couleur.depuis_rgb(235, 192, 52) + 'ATTENTION: {}'.format(texte) + couleur.FIN)
def succes(texte: str):
    """
    ## Fait un message de succès.
    
    ## Exemple:
    ```python
    from pyfrench import *

    retour.succes('Bravo, vous lisez quelque chose que personne ne lit !'`)
    ```
    """
    return print(couleur.depuis_rgb(45, 166, 49) +  'SUCCÈS: {}'.format(texte) + couleur.FIN)
def conseil(texte: str):
    """
    ## Fait un message de conseil.
    
    ## Exemple:
    ```python
    from pyfrench import *
    
    retour.conseil('https://discord.com/users/<votre id discord>')
    ```
    ### Tu verras, c'est stylé.
    """
    return print(couleur.depuis_rgb(80, 140, 212) + 'CONSEIL: {}'.format(texte) + couleur.FIN)
def message(badge: str, texte: str):
    """
    ## Fait un message de retour de console personnalisé avec badge.
    
    ## Exemple:
    ```python
    from pyfrench import *

    retour.message('MON BADGE', 'MON MESSAGE COOL !!! PK JE SUIS EN CAPS LOCK ??!!!!!!!!')
    ```
    """
    return print('{0}: {1}'.format(badge, texte) + couleur.FIN)