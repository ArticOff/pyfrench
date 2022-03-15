![MIT Licence](https://opensource.org/licenses/MIT)![PyPi version info](https://img.shields.io/pypi/v/pyfrench.svg)

# Pyfrench

> Une bibliothèque python de n'importe quelle version qui traduit ajoute la même fonctionnalité python au module.

## Pourquoi ?

Python est un excellent langage de programmation mais il est en anglais ce qui peut être un problème pour les étudiants qui ne sont pas très bilingues.
C'est pourquoi j'ai créé ce module.

## Aujourd'hui

Le projet progresse mais n'est pas terminé.
Si vous êtes intéressés, je vous laisse mon discord (Artic#6377).

Pyfrench facilite aussi le Python, il ne se contente pas de le traduire.
Il peut par exemple faire des recherches sur YouTube ou Google, ou un exécuteur de commandes.

## Comment ça marche ?

Vous avez juste besoin de Python, rien d'autre.

## Exemples

C'est un exemple très simple de système de mot de passe.

```python
from pyfrench.console import *

mot_de_passe_bdd = demander('Entrez un mot de passe')

while Vrai:

    mot_de_passe_question = demander('Quel est votre mot de passe ?')

    if mot_de_passe_bdd == mot_de_passe_question:
        afficher(couleur.VERT + couleur.GRAS + 'Bienvenue !' + couleur.FIN)
        break
    
    else:
        afficher(couleur.ROUGE + couleur.GRAS + 'Mot de passe incorrect !' + couleur.FIN)
```

Voici un réelle exemple.
Ici, un programme qui lance Google Chrome avec les termes que vous avez recherchés.

```python
from pyfrench.console import *

terminal.write('cls')

while Vrai:

    recherche = demander('Entrez un terme de recherche')
    google_recherche = google(recherche)
    terminal.write('start chrome {}'.format(google_recherche))
```

## Installation

Attention, j'ai besoin de TOUTE votre attention,

Il vous faut éxecuter la commande dans un terminal :

### Avec PIP

```
pip install pyfrench
```

### Sans PIP

```
py -3 -m pip install -U pyfrench
```

C'est tout :)

### Sur ceux, ciao !
