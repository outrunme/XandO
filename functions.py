import random


def print_game_state(game_state):
    print(*game_state[0:1])
    print(*game_state[1:4])
    print(*game_state[4:6], sep="\n")
    print(*game_state[6:9])
    print(*game_state[9:11], sep="\n")
    print(*game_state[11:14])
    print(*game_state[14:16])


def change_game_state(game_state, player, symbol, used_spots, matrix):
    if player in used_spots:
        print("Invalid Input : Used space")
    elif player == 1:
        matrix[0][0] = 1
        game_state[1] = " " + symbol
    elif player == 2:
        matrix[0][1] = 1
        game_state[2] = "| " + symbol + " |"
    elif player == 3:
        matrix[0][2] = 1
        game_state[3] = "" + symbol + " "
    elif player == 4:
        matrix[1][0] = 1
        game_state[6] = " " + symbol
    elif player == 5:
        matrix[1][1] = 1
        game_state[7] = "| " + symbol + " |"
    elif player == 6:
        matrix[1][2] = 1
        game_state[8] = "" + symbol + " "
    elif player == 7:
        matrix[2][0] = 1
        game_state[11] = " " + symbol
    elif player == 8:
        matrix[2][1] = 1
        game_state[12] = "| " + symbol + " |"
    elif player == 9:
        matrix[2][2] = 1
        game_state[13] = "" + symbol + " "
    else:
        print("Invalid Input : Not a number from 1-9")


def check(player, player_name):
    if (
        {1, 2, 3} <= set(player)
        or {4, 5, 6} <= set(player)
        or {7, 8, 9} <= set(player)
        or {1, 4, 7} <= set(player)
        or {2, 5, 8} <= set(player)
        or {3, 6, 9} <= set(player)
        or {1, 5, 9} <= set(player)
        or {3, 5, 7} <= set(player)
    ):
        print(" GAME OVER!")
        print(player_name + " wins!!")


def update(player, sentinel):
    if (
        {1, 2, 3} <= set(player)
        or {4, 5, 6} <= set(player)
        or {7, 8, 9} <= set(player)
        or {1, 4, 7} <= set(player)
        or {2, 5, 8} <= set(player)
        or {3, 6, 9} <= set(player)
        or {1, 5, 9} <= set(player)
        or {3, 5, 7} <= set(player)
    ):
        sentinel = True
        return sentinel
    else:
        sentinel = False
        return sentinel


def comp_ai(open_spots):
    chosen = random.choice(open_spots)
    return chosen


def idiocy_updater(player_input, used_spaces, idiocy_check):
    a = set()
    a.add(player_input)
    if not a <= ({1, 2, 3, 4, 5, 6, 7, 8, 9} - set(used_spaces)):
        idiocy_check += 1
        return idiocy_check
    else:
        idiocy_check = 0
        return idiocy_check


def idiocy_punisher(idiocy_check, used_spaces):
    if idiocy_check > 70:
        print("")
    elif idiocy_check > 69:
        print("Congratulations. Don't understand? You will soon.")
        f = open("consequences.txt", "w")
        print(
            "We're no strangers to love\nYou know the rules and so do I (Do I)\nA full commitment's what I'm thinking of\nYou wouldn't get this from any other guy\nI just wanna tell you how I'm feeling\nGotta make you understand\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\nWe've known each other for so long\nYour heart's been aching, but you're too shy to say it (To say it)\nInside, we both know what's been going on (Going on)\nWe know the game, and we're gonna play it\nYou might also like\nAnd if you ask me how I'm feeling\nDon't tell me you're too blind to see\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\nOoh (Give you up)\nOoh-ooh (Give you up)\nOoh-ooh\nNever gonna give, never gonna give (Give you up)\nOoh-ooh\nNever gonna give, never gonna give (Give you up)\nWe've known each other for so long\nYour heart's been aching, but you're too shy to say it (To say it)\nInside, we both know what's been going on (Going on)\nWe know the game, and we're gonna play it\nI just wanna tell you how I'm feeling\nGotta make you understand\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you",
            file=f,
        )
        f.close()
    elif idiocy_check > 68:
        print("I bet nobody loves you.")
    elif idiocy_check > 67:
        print("You're damn annoying you know that?")
    elif idiocy_check > 66:
        print("...You have to admit, I nearly got you.")
    elif idiocy_check > 18:
        print("")
    elif idiocy_check > 17:
        print(
            "Fine then, have it your way. Lets see who wins in a battle of attrition."
        )
    elif idiocy_check > 16:
        print("Fearless are we? Look everyone, we have brave heart here!")
    elif idiocy_check > 15:
        print(*list({1, 2, 3, 4, 5, 6, 7, 8, 9} - set(used_spaces))), print("Chop,Chop")
    elif idiocy_check > 14:
        print("I know you don't get 25 GBs of homework.")
    elif idiocy_check > 13:
        print(
            'Yeah... wouldn\'t want me to "Accidentally" leak your HOMEWORK folder now would you?'
        )
    elif idiocy_check > 12:
        print("Or perhaps an embarrassing incident?")
    elif idiocy_check > 11:
        print("I reckon an old-fashioned beating would do ya good.")
    elif idiocy_check > 10:
        print("You're really looking for a drubbing ain't ya?")
    elif idiocy_check > 9:
        print(
            "Listen here, you little shit. I dont know who you think you are, but do NOT test my patience."
        )
    elif idiocy_check > 8:
        print(
            "Look. I have better things to do. You have better things to do. So what are we doing here?"
        )
    elif idiocy_check > 7:
        print("Come now. You're better than this.")
    elif idiocy_check > 6:
        print("...You're really doing this?")
    elif idiocy_check > 5:
        print(
            "Lets get this over with now, shall we? Just in case you need a reminder - "
        ), print(*list({1, 2, 3, 4, 5, 6, 7, 8, 9} - set(used_spaces)))
    elif idiocy_check > 4:
        print("I have a life outside of this stupid game.")
    elif idiocy_check > 3:
        print("What do you think we're doing here?")
    elif idiocy_check > 2:
        print("The only valid inputs are"), print(
            *list({1, 2, 3, 4, 5, 6, 7, 8, 9} - set(used_spaces))
        )
    elif idiocy_check > 1:
        print("That's not a valid input.")
    elif idiocy_check > 0:
        print("Warning: Invalid Input.")
