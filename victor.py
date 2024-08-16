import random
from termcolor import colored


def generer_nombre_mystere():
    """
    Génère un nombre aléatoire entre 1 et 100.
    """
    while True:
        print("1. Facile - 10")
        print("2. Moyen - 100")
        print("3. Difficile - 1'000")
        print("4. Impossible - 10'000")
        reponse = int(input("\nQuel niveau de difficulté ?"))
        if reponse == 1:
            max = 10
            break
        if reponse == 2:
            max = 100
        if reponse == 3:
            max = 1000
            break
        if reponse == 4:
            max = 10000

    x = random.randint(1, max)
    return x, max


def demander_saisie(max):
    """
    Demande au joueur de saisir un nombre.
    """
    while True:
        reponse = input(f"\nDevine le nombre caché entre 1 et {max} : ")
        if reponse.isdigit():
            return int(reponse)
        else:
            print("Mets un nombre pupuce !")


def verifier_nombre(nombre_joueur, nombre_mystere):
    """
    Vérifie si le nombre du joueur est égal au nombre mystère.
    """
    if nombre_joueur == nombre_mystere:
        return True
    else:
        return False


def donner_indice(nombre_joueur, nombre_mystere):
    """
    Donne un indice au joueur.
    """

    if nombre_mystere < nombre_joueur:
        print("\nPlus petit, ne soit pas gourmand mon garçon ! ")
    if nombre_mystere > nombre_joueur:
        print("\nPlus grand, vers l'infini et au-delà")


def score_manager(score_actuel, meilleur_score):
    if score_actuel < meilleur_score or meilleur_score == 0:
        print(colored("Nouveau meilleur score !", "red"))
        return score_actuel


def jouer_partie(n, bs):
    """
    Gère le déroulement de la partie.
    """
    counter = 0
    nombre_mystere, max = generer_nombre_mystere()
    if not bs == 0:
        print("\nMeilleur score :" + str(bs))
    while True:
        reponse = demander_saisie(max)
        if verifier_nombre(reponse, nombre_mystere):
            counter = counter + 1
            print(colored("\nBien joué " + n + ", tu as gagné en " + str(counter) + " essais 👑\n", "green"))
            bs = score_manager(counter, bs)
            while True:
                r = input(colored("\nVeux tu rejouer 🔄️ ? ", "blue"))
                if r == "oui" or r == "Oui":
                    jouer_partie(n, bs)
                if r == "non" or r == "Non":
                    print("D'accord, à la prochaine 👋\n")
                    exit()
                else:
                    print("J'ai pas compris, choisis entre \"oui ou non\"\n ")

        else:
            donner_indice(reponse, nombre_mystere)
            counter = counter + 1


def main():
    """
    Fonction principale du jeu.
    """
    n = input("Entre un pseudo : \n")
    bs = 0
    jouer_partie(n, bs)


if __name__ == "__main__":
    main()