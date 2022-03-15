<a href="https://discord.gg/GM2wSefRUT"><img src="https://discord.com/api/guilds/903297618728349736/embed.png" alt="Discord" height="18"></a> ![MIT Licence](https://warehouse-camo.ingress.cmh1.psfhosted.org/f564a2fa3d89c69619dfabf8a770353094df052f/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6a776f646465722f707976657273696f6e2d696e666f2e737667) <a href="https://badge.fury.io/py/pyfrench"><img src="https://badge.fury.io/py/pyfrench.svg" alt="PyPI version" height="18"></a>
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
