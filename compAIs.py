import random


def random_choice(open_spots):
    chosen = random.choice(open_spots)
    return chosen


def algorithmic_choice(used_spaces, open_spaces, computer_spaces, player_spaces):
    chosen = random.choice(open_spaces)
    if {1, 2}.issubset(computer_spaces) and (not {3}.issubset(used_spaces)):
        chosen = 3
    elif {4, 5}.issubset(computer_spaces) and (not {6}.issubset(used_spaces)):
        chosen = 6
    elif {7, 8}.issubset(computer_spaces) and (not {9}.issubset(used_spaces)):
        chosen = 9
    elif {1, 4}.issubset(computer_spaces) and (not {7}.issubset(used_spaces)):
        chosen = 7
    elif {2, 5}.issubset(computer_spaces) and (not {8}.issubset(used_spaces)):
        chosen = 8
    elif {3, 6}.issubset(computer_spaces) and (not {9}.issubset(used_spaces)):
        chosen = 9
    elif {1, 5}.issubset(computer_spaces) and (not {9}.issubset(used_spaces)):
        chosen = 9
    elif {3, 5}.issubset(computer_spaces) and (not {7}.issubset(used_spaces)):
        chosen = 7
    elif {1, 3}.issubset(computer_spaces) and (not {2}.issubset(used_spaces)):
        chosen = 2
    elif {4, 6}.issubset(computer_spaces) and (not {5}.issubset(used_spaces)):
        chosen = 5
    elif {7, 9}.issubset(computer_spaces) and (not {8}.issubset(used_spaces)):
        chosen = 8
    elif {1, 7}.issubset(computer_spaces) and (not {4}.issubset(used_spaces)):
        chosen = 4
    elif {2, 8}.issubset(computer_spaces) and (not {5}.issubset(used_spaces)):
        chosen = 5
    elif {3, 9}.issubset(computer_spaces) and (not {6}.issubset(used_spaces)):
        chosen = 6
    elif {1, 9}.issubset(computer_spaces) and (not {5}.issubset(used_spaces)):
        chosen = 5
    elif {3, 7}.issubset(computer_spaces) and (not {5}.issubset(used_spaces)):
        chosen = 5
    elif {3, 2}.issubset(computer_spaces) and (not {1}.issubset(used_spaces)):
        chosen = 1
    elif {6, 5}.issubset(computer_spaces) and (not {4}.issubset(used_spaces)):
        chosen = 4
    elif {9, 8}.issubset(computer_spaces) and (not {7}.issubset(used_spaces)):
        chosen = 7
    elif {7, 4}.issubset(computer_spaces) and (not {1}.issubset(used_spaces)):
        chosen = 1
    elif {8, 5}.issubset(computer_spaces) and (not {2}.issubset(used_spaces)):
        chosen = 2
    elif {9, 6}.issubset(computer_spaces) and (not {3}.issubset(used_spaces)):
        chosen = 3
    elif {9, 5}.issubset(computer_spaces) and (not {1}.issubset(used_spaces)):
        chosen = 1
    elif {7, 5}.issubset(computer_spaces) and (not {3}.issubset(used_spaces)):
        chosen = 3
    elif {1, 2}.issubset(player_spaces) and (not {3}.issubset(used_spaces)):
        chosen = 3
    elif {4, 5}.issubset(player_spaces) and (not {6}.issubset(used_spaces)):
        chosen = 6
    elif {7, 8}.issubset(player_spaces) and (not {9}.issubset(used_spaces)):
        chosen = 9
    elif {1, 4}.issubset(player_spaces) and (not {7}.issubset(used_spaces)):
        chosen = 7
    elif {2, 5}.issubset(player_spaces) and (not {8}.issubset(used_spaces)):
        chosen = 8
    elif {3, 6}.issubset(player_spaces) and (not {9}.issubset(used_spaces)):
        chosen = 9
    elif {1, 5}.issubset(player_spaces) and (not {9}.issubset(used_spaces)):
        chosen = 9
    elif {3, 5}.issubset(player_spaces) and (not {7}.issubset(used_spaces)):
        chosen = 7
    elif {1, 3}.issubset(player_spaces) and (not {2}.issubset(used_spaces)):
        chosen = 2
    elif {4, 6}.issubset(player_spaces) and (not {5}.issubset(used_spaces)):
        chosen = 5
    elif {7, 9}.issubset(player_spaces) and (not {8}.issubset(used_spaces)):
        chosen = 8
    elif {1, 7}.issubset(player_spaces) and (not {4}.issubset(used_spaces)):
        chosen = 4
    elif {2, 8}.issubset(player_spaces) and (not {5}.issubset(used_spaces)):
        chosen = 5
    elif {3, 9}.issubset(player_spaces) and (not {6}.issubset(used_spaces)):
        chosen = 6
    elif {1, 9}.issubset(player_spaces) and (not {5}.issubset(used_spaces)):
        chosen = 5
    elif {3, 7}.issubset(player_spaces) and (not {5}.issubset(used_spaces)):
        chosen = 5
    elif {3, 2}.issubset(player_spaces) and (not {1}.issubset(used_spaces)):
        chosen = 1
    elif {6, 5}.issubset(player_spaces) and (not {4}.issubset(used_spaces)):
        chosen = 4
    elif {9, 8}.issubset(player_spaces) and (not {7}.issubset(used_spaces)):
        chosen = 7
    elif {4, 7}.issubset(player_spaces) and (not {1}.issubset(used_spaces)):
        chosen = 1
    elif {5, 8}.issubset(player_spaces) and (not {2}.issubset(used_spaces)):
        chosen = 2
    elif {6, 9}.issubset(player_spaces) and (not {3}.issubset(used_spaces)):
        chosen = 3
    elif {5, 9}.issubset(player_spaces) and (not {1}.issubset(used_spaces)):
        chosen = 1
    elif {7, 5}.issubset(player_spaces) and (not {3}.issubset(used_spaces)):
        chosen = 3
    return chosen
