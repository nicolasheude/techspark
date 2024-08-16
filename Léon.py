import random
from termcolor import colored


def get_player_names():
    """Asks for the players' names."""
    player1_name = input(colored("\nentre le nom du premier joueur: ", "blue"))
    player2_name = input(colored("\nentre le nom du deuxième joueur: ", "blue"))
    print(colored(f'\nles deux joueurs son {player1_name} vs {player2_name}.', "red"))
    list_player = [player1_name, player2_name]
    return list_player


def get_number_of_matches():
    """Asks for the number of matches at the beginning of the game."""
    matches_left = input(colored("\ncombien d allumette veux tu: ", "blue"))
    print(colored(f'\n{matches_left} allumette.', "red"))
    return int(matches_left)


def play_round(current_player_name, matches_left, ia=False):
    if ia == False:
        print(colored(f'\nil reste {matches_left} allumette.', "red"))
        print(colored(f'\nc\'est a: {current_player_name}.', "red"))
    if ia == True:
        x = random.randint(1, 3)
        print(colored(f"\nIA a retirer {x} allumettes", "red"))
        return matches_left - x
    else:
        while True:
            choix = int(input(colored("\nCombien d'allumette veux-tu enlever 1,2 ou 3: ", "blue")))
            if choix == 1:
                return matches_left - 1
            elif choix == 2:
                return matches_left - 2
            elif choix == 3:
                return matches_left - 3


def check_game_end(matches_left):
    """Checks if the game is over."""
    if matches_left <= 0:
        return True
    else:
        return False


def play_against_player(player1_name, player2_name, matches):
    """Allows two players to compete."""
    while True:
        matches = play_round(player1_name, matches)
        if check_game_end(matches) == True:
            print(colored(f'{player1_name} a gagner.', "red"))
            break
        matches = play_round(player2_name, matches)
        if check_game_end(matches) == True:
            print(colored(f'{player2_name} a gagner.', "red"))
            break


def play_against_random_ai(player1_name, matches):
    """Allows a player to play against a random AI."""
    while True:
        matches = play_round(player1_name, matches)
        if check_game_end(matches) == True:
            print(f'{player1_name} a gagner.')
            break
        matches = play_round("ai", matches, True)
        if check_game_end(matches) == True:
            print(f'{"ai"} a gagner.')
            break


def play_against_avoid_errors_ai(player_name, matches):
    """Allows a player to play against an AI that avoids basic errors."""
    while True:
        matches = play_round(player_name, matches)
        if check_game_end(matches) == True:
            print(f'{list_player} a gagner.')
            break
        if matches % 4 == 1:
            matches = matches - 1
            print(colored(f"\nIA a retirer 1 allumettes", "red"))
        elif matches % 4 == 2:
            matches = matches - 2
            print(colored(f"\nIA a retirer 2 allumettes", "red"))
        elif matches % 4 == 3:
            matches = matches - 3
            print(colored(f"\nIA a retirer 3 allumettes", "red"))
        elif matches % 4 == 0:
            x = random.randint(1, 3)
            matches = matches - x
            print(colored(f"\nIA a retirer {x} allumettes", "red"))
        if check_game_end(matches) == True:
            print(colored(f'\nIA a gagner.', "red"))
            break


# Start of the game
while True:
    list_player = get_player_names()
    matches_left = get_number_of_matches()

    print(colored("\n1: joueur", "green"))
    print(colored("2: IA normal", "green"))
    print(colored("3: IA difficile", "green"))
    qui = int(input(colored("\navec qui tu veux jouer: ", "blue")))
    if qui == 1:
        play_against_player(list_player[0], list_player[1], matches_left)

    elif qui == 2:
        play_against_random_ai(list_player[0], matches_left)

    elif qui == 3:
        play_against_avoid_errors_ai(list_player[0], matches_left)
