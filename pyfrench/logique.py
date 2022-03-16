def égale(valeur1: int, valeur2: int):
    if valeur1 == valeur2:
        return True
    else:
        return False
def différentDe(valeur1: int, valeur2: int):
    if valeur1 != valeur2:
        return True
    else:
        return False
def plusGrand(valeur1: int, valeur2: int):
    if valeur1 > valeur2:
        return True
    else:
        return False
def plusPetit(valeur1: int, valeur2: int):
    if valeur1 < valeur2:
        return True
    else:
        return False 
def égalePlusGrand(valeur1: int, valeur2: int):
    if valeur1 >= valeur2:
        return True
    else:
        return False
def égalePlusPetit(valeur1: int, valeur2: int):
    if valeur1 <= valeur2:
        return True
    else:
        return False
def AND(A: int, B: int):
    return A & B
def NOT(A: int):
    return ~A+2
def XOR(x: int, y: int):
    return bool((x and not y) or (not x and y))
def NAND(A: int, B: int):
    return NOT(AND(A, B))
def OR(A: int, B: int):
    return A | B
def NOR(A: int, B: int):
    return NOT(OR(A, B))
def XNOR(A: int, B: int):
    return NOT(XOR(A, B))