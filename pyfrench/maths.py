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

from math import *

def calcul(calcul: str):
    """
    ## Effectue un calcul.
    
    ## Exemple:
    ```python
    from pyfrench import *

    maths.calcul('5*3+4')
    ```
    """
    return print(int(eval(calcul)))
def nombreNonDuplique(liste: list):
    """
    ## Trouve le nombre non dupliqué dans une liste.
    
    ## Exemple:
    ```python
    from pyfrench import *

    maths.nombreNonDuplique('5*3+4')
    ```
    """
    resultat = 0
    for e in liste:
        resultat ^= e
    return resultat
def num(nombre: str):
    """
    ## Convertit un nombre textuel en nombre entier.
    
    ## Exemple:
    ```python
    from pyfrench import *

    maths.num('42')
    ```
    """
    return int(nombre)
def txt(nombre: int):
    """
    ## Convertit un nombre entier en nombre texutel.
    
    ## Exemple:
    ```python
    from pyfrench import *

    maths.txt(42)
    ```
    """
    return str(nombre)
def inverse(nombre1: int, nombre2: int):
    """
    ## Effectue l'inverse du nombre 'nombre1' par rapport à 'nombre2'.
    
    ## Exemple:
    ```python
    from pyfrench import *

    maths.inverse(2, 5)
    ```
    """
    return nombre1 - nombre2
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679