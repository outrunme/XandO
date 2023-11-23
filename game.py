import functions
import compAIs
import random

matrix_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def game_x():
    board = [
        "   |   |   ",
        "  ",
        "|   |",
        "   ",
        "___|___|___",
        "   |   |   ",
        "  ",
        "|   |",
        "   ",
        "___|___|___",
        "   |   |   ",
        "  ",
        "|   |",
        "   ",
        "   |   |   ",
    ]
    functions.print_game_state(board)
    options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    used = set()
    player_spots = set()
    computer_spots = set()
    game_over_check = False
    idiocy_count = 0
    while used < {1, 2, 3, 4, 5, 6, 7, 8, 9}:
        if not game_over_check:
            while True:
                digit_check = input("Your move?:")
                if digit_check.isdigit():
                    player_choice = int(digit_check)
                    idiocy_count = functions.idiocy_updater(
                        player_choice, used, idiocy_count
                    )
                    functions.idiocy_punisher(idiocy_count, used)
                    if idiocy_count == 0:
                        break
                elif not digit_check.isdigit():
                    idiocy_count += 1
                    functions.idiocy_punisher(idiocy_count, used)
                elif idiocy_count == 0:
                    break
            functions.change_game_state(board, player_choice, "X", used, matrix_board)
            functions.print_game_state(board)
            used.add(player_choice)
            player_spots.add(player_choice)
            functions.check(player_spots, "Player")
            game_over_check = functions.update(player_spots, game_over_check)
            if game_over_check:
                break
            print("")
        if (used < {1, 2, 3, 4, 5, 6, 7, 8, 9}) and not game_over_check:
            open = list(set(options) - used)
            computer_choice = compAIs.algorithmic_choice(
                used, open, computer_spots, player_spots
            )
            if computer_choice in used:
                computer_choice = random.choice(open)
            functions.change_game_state(board, computer_choice, "O", used, matrix_board)
            functions.print_game_state(board)
            used.add(computer_choice)
            computer_spots.add(computer_choice)
            functions.check(computer_spots, "Computer")
            game_over_check = functions.update(computer_spots, game_over_check)
            if game_over_check:
                break


def game_o():
    board = [
        "   |   |   ",
        "  ",
        "|   |",
        "   ",
        "___|___|___",
        "   |   |   ",
        "  ",
        "|   |",
        "   ",
        "___|___|___",
        "   |   |   ",
        "  ",
        "|   |",
        "   ",
        "   |   |   ",
    ]
    functions.print_game_state(board)
    print("")
    options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    used = set()
    player_spots = set()
    computer_spots = set()
    game_over_check = False
    idiocy_count = 0
    while used < {1, 2, 3, 4, 5, 6, 7, 8, 9}:
        if not game_over_check:
            open = list(set(options) - used)
            computer_choice = compAIs.algorithmic_choice(
                used, open, computer_spots, player_spots
            )
            if computer_choice in used:
                computer_choice = random.choice(open)
            functions.change_game_state(board, computer_choice, "X", used, matrix_board)
            functions.print_game_state(board)
            used.add(computer_choice)
            computer_spots.add(computer_choice)
            functions.check(computer_spots, "Computer")
            game_over_check = functions.update(computer_spots, game_over_check)
            if game_over_check:
                break
            print("")

        if (used < {1, 2, 3, 4, 5, 6, 7, 8, 9}) and not game_over_check:
            while True:
                digit_check = input("Your move?:")
                if digit_check.isdigit():
                    player_choice = int(digit_check)
                    idiocy_count = functions.idiocy_updater(
                        player_choice, used, idiocy_count
                    )
                    functions.idiocy_punisher(idiocy_count, used)
                    if idiocy_count == 0:
                        break
                elif not digit_check.isdigit():
                    idiocy_count += 1
                    functions.idiocy_punisher(idiocy_count, used)
                elif idiocy_count == 0:
                    break
            functions.change_game_state(board, player_choice, "O", used, matrix_board)
            functions.print_game_state(board)
            used.add(player_choice)
            player_spots.add(player_choice)
            functions.check(player_spots, "Player")
            game_over_check = functions.update(player_spots, game_over_check)
            if game_over_check:
                break
            print("")
