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

def égale(valeur1: int, valeur2: int):
    """
    ## Renvoie une valeur booléenne si les deux valeurs sont égales.
    
    ## Exemple:
    ```python
    from pyfrench import *

    logique.égale(2, 2)
    ```
    """
    if valeur1 == valeur2:
        return True
    else:
        return False
def différentDe(valeur1: int, valeur2: int):
    """
    ## Renvoie une valeur booléenne si les deux valeurs sont différentes.
    
    ## Exemple:
    ```python
    from pyfrench import *

    logique.différentDe(2, 4)
    ```
    """
    if valeur1 != valeur2:
        return True
    else:
        return False
def plusGrand(valeur1: int, valeur2: int):
    """
    ## Renvoie une valeur booléenne si la première valeur est supérieure à la seconde.
    
    ## Exemple:
    ```python
    from pyfrench import *

    logique.plusGrand(3, 2)
    ```
    """
    if valeur1 > valeur2:
        return True
    else:
        return False
def plusPetit(valeur1: int, valeur2: int):
    """
    ## Renvoie une valeur booléenne si la première valeur est plus petite que la seconde.
    
    ## Exemple:
    ```python
    from pyfrench import *

    logique.plusPetit(6, 1)
    ```
    """
    if valeur1 < valeur2:
        return True
    else:
        return False 
def égalePlusGrand(valeur1: int, valeur2: int):
    """
    ## Renvoie une valeur booléenne si la première valeur est égale ou supérieure à la seconde.
    
    ## Exemple:
    ```python
    from pyfrench import *

    logique.égalePlusGrand(7, 15)
    ```
    """
    if valeur1 >= valeur2:
        return True
    else:
        return False
def égalePlusPetit(valeur1: int, valeur2: int):
    """
    ## Renvoie une valeur booléenne si la première valeur est égale ou inférieure à la seconde.
    
    ## Exemple:
    ```python
    from pyfrench import *

    logique.égalePlusPetit(4, 11)
    ```
    """
    if valeur1 <= valeur2:
        return True
    else:
        return False
def est(valeur1: int, valeur2: int):
    """
    ## Renvoie une valeur booléenne si la première valeur est la seconde.
    
    ## Exemple:
    ```python
    from pyfrench import *

    logique.est(5, 5)
    ```
    """
    return valeur1 is valeur2
def pas(valeur1: int, valeur2: int):
    """
    ## Ne renvoie aucune valeur booléenne si la première valeur est la seconde.
    
    ## Exemple:
    ```python
    from pyfrench import *

    logique.pas(3, 3)
    ```
    """
    return valeur1 is not valeur2
def AND(A: int, B: int):
    """## Porte logique AND"""
    return A & B
def NOT(A: int):
    """## Porte logique NOT"""
    return ~A+2
def XOR(x: int, y: int):
    """## Porte logique XOR"""
    return bool((x and not y) or (not x and y))
def NAND(A: int, B: int):
    """## Porte logique NAND"""
    return NOT(AND(A, B))
def OR(A: int, B: int):
    """## Porte logique OR"""
    return A | B
def NOR(A: int, B: int):
    """## Porte logique NOR"""
    return NOT(OR(A, B))
def XNOR(A: int, B: int):
    """## Porte logique XNOR"""
    return NOT(XOR(A, B))