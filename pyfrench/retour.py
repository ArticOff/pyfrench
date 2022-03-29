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

def erreur(erreur: str):
    """
    ## Fait un message d'erreur.
    
    ## Exemple:
    ```python
    from pyfrench import *

    retour.erreur('Pain au chocolat, pas chocolatine')
    ```
    ### J'ai rien contre vous les gens du sud-ouest, vous êtes les best !!!
    """
    return print('\033[38;2;255;0;0m' + 'ERREUR: {}'.format(erreur) + '\033[0m')
def attention(texte: str):
    """
    ## Fait un message de prévention.
    
    ## Exemple:
    ```python
    from pyfrench import *

    retour.attention('1+1 = 3, pas 2...')
    """
    return print('\033[38;2;235;192;52m' + 'ATTENTION: {}'.format(texte) + '\033[0m')
def succes(texte: str):
    """
    ## Fait un message de succès.
    
    ## Exemple:
    ```python
    from pyfrench import *

    retour.succes('Bravo, vous lisez quelque chose que personne ne lit !'`)
    ```
    """
    return print('\033[38;2;45;166;49m' +  'SUCCÈS: {}'.format(texte) + '\033[0m')
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
    return print('\033[38;2;80;140;212m' + 'CONSEIL: {}'.format(texte) + '\033[0m')
def message(badge: str, texte: str):
    """
    ## Fait un message de retour de console personnalisé avec badge.
    
    ## Exemple:
    ```python
    from pyfrench import *

    retour.message('MON BADGE', 'MON MESSAGE COOL !!! PK JE SUIS EN CAPS LOCK ??!!!!!!!!')
    ```
    """
    return print('{0}: {1}'.format(badge, texte) + '\033[0m')