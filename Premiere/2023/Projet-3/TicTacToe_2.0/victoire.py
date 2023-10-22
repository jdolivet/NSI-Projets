import pyxel

def victoire(case_dict, tour_joueur):
    possibles_victoires = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]]

    for combination in possibles_victoires:
        if all(case_dict[i] == tour_joueur for i in combination):
            return True

    return False

    