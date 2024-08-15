## Projet "Just Price" en Python:

**Objectif:** Créer un jeu "Just Price" où l'ordinateur choisit un nombre aléatoire entre 1 et 100 et le joueur doit le deviner en un minimum d'essais.

**Instructions:**

1. **Créer un fichier Python nommé `just_price.py`**

2. **Créer les fonctions suivantes:**

   * **`generer_nombre_mystere()`:**  Cette fonction doit générer un nombre aléatoire entre 1 et 100 et le retourner.

   * **`demander_saisie()`:** Cette fonction doit demander au joueur de saisir un nombre et le retourner.

   * **`verifier_nombre(nombre_joueur, nombre_mystere)`:**  Cette fonction doit vérifier si le nombre du joueur est égal au nombre mystère. Si oui, elle retourne `True`, sinon `False`.

   * **`donner_indice(nombre_joueur, nombre_mystere)`:** Cette fonction doit donner un indice au joueur en lui indiquant si son nombre est plus grand ou plus petit que le nombre mystère.

   * **`jouer_partie()`:**  Cette fonction doit gérer le déroulement de la partie. Elle doit appeler les autres fonctions pour générer le nombre mystère, demander la saisie, vérifier le nombre, donner des indices et gérer la victoire ou la défaite.

3. **Créer la fonction principale `main()`:**
   * Cette fonction doit appeler la fonction `jouer_partie()` pour lancer le jeu.

4. **Ajouter la ligne suivante à la fin du fichier `just_price.py`:**

   ```python
   if __name__ == "__main__":
       main()
   ```

**Base de code:**

```python
import random

def generer_nombre_mystere():
    """
    Génère un nombre aléatoire entre 1 et 100.
    """
    # À compléter

def demander_saisie():
    """
    Demande au joueur de saisir un nombre.
    """
    # À compléter

def verifier_nombre(nombre_joueur, nombre_mystere):
    """
    Vérifie si le nombre du joueur est égal au nombre mystère.
    """
    # À compléter

def donner_indice(nombre_joueur, nombre_mystere):
    """
    Donne un indice au joueur.
    """
    # À compléter

def jouer_partie():
    """
    Gère le déroulement de la partie.
    """
    # À compléter

def main():
    """
    Fonction principale du jeu.
    """
    jouer_partie()

if __name__ == "__main__":
    main()
```

**Défi:**  

* Complète les fonctions vides en utilisant les instructions données dans les commentaires.
* N'oublie pas d'utiliser les fonctions que tu as créées dans la fonction `jouer_partie()`.
* Pense à ajouter des messages d'accueil, des instructions et des messages de victoire/défaite pour rendre le jeu plus interactif.

**Conseils:**

* N'hésite pas à tester ton code après chaque fonction que tu complètes.
* Utilise des variables pour stocker les informations importantes, comme le nombre mystère, le nombre d'essais, etc.
* Pense à utiliser des structures conditionnelles (if, elif, else) pour gérer les différentes situations du jeu.

**Amuse-toi bien à créer ton propre jeu Just Price!**


- [x] Afficher entre quels nombres il doit deviner.
- [x] Demander le nom du joueur.
- [x] À la fin d'une partie, lui donner l'option de rejouer.
- [x] Afficher s'il a battu son record d'essais.

### Next step:

- [ ] Permettre la saisie d'un nombre uniquement.
- [ ] Améliorer l'affichage des messages print.
- [ ] Ajouter le choix de plusieurs niveaux (facile: 0 - 10), (moyen: 0 - 100), (difficile: 0 - 1000), (impossible: 0 - 10 000)
- [ ] Ajouter un mode avec un nombre d'essais limité.
- [ ] Sauvegarder le score des joueurs dans un fichier sur l'ordinateur.
