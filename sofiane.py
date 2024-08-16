import random
from termcolor import colored


def get_player_names():
    p1_name = input(colored("player 1's name ", "black"))
    p2_name = input(colored("player 2's name ", "black"))
    print(colored(f'{p1_name} vs {p2_name}', "black"))
    list_of_names = [p1_name, p2_name]
    return list_of_names


def get_number_of_matches():
    number_of_matches = int(input(colored("how many matches do you want ", "black")))
    print(colored(f'there will be {number_of_matches} matches', "black"))
    return number_of_matches


def play_round(current_player_name, matches_left, ia=False):
    ## print(f'there are {matches_left} and it is {current_player_name}s turn')
    ## matches_to_remove=input("how many matches would you like to remove")

    while True:
        print(colored(f'there are {matches_left} matches and it is {current_player_name}\'s turn', "black"))
        if ia == True:
            return matches_left - random.randint(1, 3)
        else:
            matches_to_remove = int(input(colored("how many matches would you like to remove: ", "black")))
            if matches_to_remove == 1:
                return matches_left - 1
            elif matches_to_remove == 2:
                return matches_left - 2
            elif matches_to_remove == 3:
                return matches_left - 3
            else:
                print(colored("please enter a valid number", "black"))


def check_game_end(matches_left):
    is_game_over = False
    if int(matches_left) <= 0:
        is_game_over = True
    else:
        is_game_over = False
    return is_game_over


def play_against_player(player1_name, player2_name, matches, who_starts):
    """Allows two players to compete."""
    while True:
        if who_starts == 1:
            matches = play_round(player1_name, matches)
            who_starts = 2
            if check_game_end(matches) == True:
                print(colored(f'{player1_name} won', "black"))
                break
        else:
            matches = play_round(player2_name, matches)
            who_starts = 1
            if check_game_end(matches) == True:
                print(colored(f'{player2_name} won', "black"))
                break


def play_against_random_ai(player_name, matches, who_starts, ia=False):
    while True:
        if who_starts == 1:
            matches = play_round(player_name, matches)
            who_starts = 2
            if check_game_end(matches) == True:
                print(colored(f'{player_name} won', "black"))
                break
        else:
            matches = play_round("ai", matches, True)
            who_starts = 1
            if check_game_end(matches) == True:
                print(colored(f'ai won', "black"))
                break


def play_against_avoid_errors_ai(player_name, matches, who_starts):
    while True:
        if who_starts == 1:
            matches = play_round(player_name, matches)
            who_starts = 2
            if check_game_end(matches) == True:
                print(colored(f'{player_name} won', "black"))
                break
        else:
            who_starts = 1
            if matches % 4 == 0:
                temp = random.randint(1, 3)
                matches = matches - temp
                print(colored(f'the ai removed {temp} matches', "black"))
                continue
            if matches % 4 == 1:
                matches = matches - 1
                print(colored(f'the ai removed 1 matches', "black"))
                continue
            if matches % 4 == 2:
                matches = matches - 2
                print(colored(f'the ai removed 2 matches', "black"))
                continue
            if matches % 4 == 3:
                matches = matches - 3
                print(colored(f'the ai removed 3 matches', "black"))
                continue
            if check_game_end(matches) == True:
                print(colored(f'ai won', "black"))
                break


while True:
    player_names = get_player_names()
    number_of_matches = get_number_of_matches()
    who_starts = random.randint(1, 2)
    print(colored("who would you like to play against\n", "black"))
    pagainst = int(input(colored("""1)another player
2)a random ai
3)an ai that avoids errors\n""", "black")))
    if pagainst == 2:
        play_against_random_ai(player_names[0], number_of_matches, who_starts, True)
    elif pagainst == 3:
        play_against_avoid_errors_ai(player_names[0], number_of_matches, who_starts)
    elif pagainst == 1:
        play_against_player(player_names[0], player_names[1], number_of_matches, who_starts)
    else:
        print(colored("please enter a valid character", "black"))
##copywrite 2024 all rights reserved
