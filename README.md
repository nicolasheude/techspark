## Le Jeu des Allumettes : Maitrisez la Stratégie !

**Objectif:** Créer un jeu en Python où deux joueurs s'affrontent en retirant des allumettes d'un tas. Le joueur qui retire la dernière allumette gagne ! 

**Règles du jeu:**

1. **Le tas d'allumettes:** Au début du jeu, il y a un certain nombre d'allumettes sur le terrain (vous pouvez choisir ce nombre).
2. **Les joueurs:** Il y a deux joueurs : le joueur 1 et le joueur 2. 
3. **Le tour de jeu:** Chaque joueur à son tour doit retirer 1, 2 ou 3 allumettes du tas.
4. **Fin du jeu:** Le joueur qui retire la dernière allumette remporte la partie !

**Votre mission:**

Créer un programme Python qui permet de jouer au jeu des allumettes. Voici les étapes à suivre :

1. **Fonction `get_player_names` :**
   - Cette fonction demande le nom des joueurs.
   - Elle renvoie une liste contenant les noms des deux joueurs.

2. **Fonction `get_number_of_matches` :**
   - Cette fonction demande le nombre d'allumettes au début du jeu.
   - Elle renvoie le nombre d'allumettes choisi par les joueurs.

3. **Fonction `play_round` :**
   - Cette fonction permet de jouer un tour du jeu.
   - Elle prend en arguments le nom du joueur actuel, le nombre d'allumettes restantes et un booléen indiquant si l'IA joue (True si l'IA joue, False sinon).
   - Si l'IA joue, elle choisit un nombre d'allumettes à retirer de manière aléatoire.
   - Si le joueur humain joue, la fonction lui demande combien d'allumettes il veut retirer.
   - La fonction vérifie si le joueur a entré un nombre valide (entre 1 et 3).
   - La fonction retire le nombre d'allumettes choisi du tas et renvoie le nouveau nombre d'allumettes restantes.

4. **Fonction `check_game_end` :**
   - Cette fonction vérifie si la partie est terminée.
   - Elle prend en argument le nombre d'allumettes restantes.
   - Si le nombre d'allumettes est à 0, la fonction renvoie True, indiquant que la partie est terminée. Sinon, elle renvoie False.

5. **Fonction `play_against_player` :**
   - Cette fonction permet à deux joueurs de s'affronter.
   - Elle prend en arguments les noms des deux joueurs et le nombre d'allumettes au début.
   - La fonction utilise les fonctions `play_round` et `check_game_end` pour gérer les tours du jeu.
   - La fonction affiche le nom du vainqueur à la fin de la partie.

6. **Fonction `play_against_random_ai` :**
   - Cette fonction permet à un joueur de jouer contre une IA qui choisit aléatoirement combien d'allumettes retirer.
   - Elle prend en arguments le nom du joueur et le nombre d'allumettes au début.
   - La fonction utilise les fonctions `play_round` et `check_game_end` pour gérer les tours du jeu.
   - L'IA choisit un nombre d'allumettes à retirer aléatoirement entre 1 et 3.
   - La fonction affiche le nom du vainqueur à la fin de la partie.

7. **Fonction `play_against_avoid_errors_ai` :**
   - Cette fonction permet à un joueur de jouer contre une IA qui essaie d'éviter les erreurs basiques.
   - Elle prend en arguments le nom du joueur et le nombre d'allumettes au début.
   - La fonction utilise les fonctions `play_round` et `check_game_end` pour gérer les tours du jeu.
   - L'IA utilise une stratégie simple pour essayer de forcer le joueur à faire la dernière prise. Par exemple, si le nombre d'allumettes est un multiple de 4, l'IA peut retirer 1 allumette pour laisser le joueur face à un nombre d'allumettes multiple de 4.
   - La fonction affiche le nom du vainqueur à la fin de la partie.

8. **Fonction `play_against_ultra_strong_ai` :**
   - Cette fonction permet à un joueur de jouer contre une IA qui utilise une stratégie gagnante.
   - Elle prend en arguments le nom du joueur et le nombre d'allumettes au début.
   - La fonction utilise les fonctions `play_round` et `check_game_end` pour gérer les tours du jeu.
   - L'IA utilise une stratégie pour forcer le joueur à faire la dernière prise, en utilisant un algorithme pour choisir les meilleurs mouvements possibles.
   - La fonction affiche le nom du vainqueur à la fin de la partie.

9. **Créer un menu principal :**
   - Demandez au joueur de choisir un mode de jeu :
     - Jouer contre un autre joueur
     - Jouer contre une IA aléatoire
     - Jouer contre une IA qui évite les erreurs basiques
     - Jouer contre une IA ultra forte

10. **Lancer le jeu en fonction du choix du joueur :**
    - Appelez la fonction correspondante en fonction du choix du joueur.

**Code de base :**

```python
import random

def get_player_names():
  """Asks for the players' names."""
  # ... (To be completed) ...

def get_number_of_matches():
  """Asks for the number of matches at the beginning of the game."""
  # ... (To be completed) ...

def play_round(current_player_name, matches_left, ia=False):
  """Allows to play a round of the game."""
  # ... (To be completed) ...

def check_game_end(matches_left):
  """Checks if the game is over."""
  # ... (To be completed) ...

def play_against_player(player1_name, player2_name, matches):
  """Allows two players to compete."""
  # ... (To be completed) ...

def play_against_random_ai(player_name, matches):
  """Allows a player to play against a random AI."""
  # ... (To be completed) ...

def play_against_avoid_errors_ai(player_name, matches):
  """Allows a player to play against an AI that avoids basic errors."""
  # ... (To be completed) ...

def play_against_ultra_strong_ai(player_name, matches):
  """Allows a player to play against an ultra-strong AI."""
  # ... (To be completed) ...

# Start of the game
while True:
  # ... (To be completed) ...
```

**Conseils:**

- Utilisez les fonctions `input()` pour obtenir les entrées du joueur.
- Utilisez des boucles `while` pour répéter les tours de jeu.
- Utilisez des conditions `if` pour gérer les différentes actions du joueur.
- Utilisez la fonction `random.randint()` pour générer des nombres aléatoires pour l'IA.
- Utilisez des variables pour stocker le nombre d'allumettes restantes et le nom des joueurs.

**Améliorations possibles:**

- Vous pouvez ajouter des fonctionnalités supplémentaires, comme :
    - Afficher le score des joueurs.
    - Demander aux joueurs s'ils veulent jouer à nouveau.
    - Créer une interface graphique plus attrayante.
    - Implémenter des IA plus complexes.

**Bon courage et amusez-vous à créer votre jeu des allumettes !**
