import game
from os.path import exists

if exists("consequences.txt"):
    banishment = "yes"
    print("Look in consequences.txt")
else:
    banishment = "no"

if banishment == "no":
    response = input("Hi! Wanna play X and O? (Y/N):")

    def game_start():
        if response == "N" or response == "n":
            return "OK. I have nothing else for you. Go away now."
        if response == "Y" or response == "y":
            return "Sure! Let's Play"

    start = game_start()
    print(start)

    if response == "Y" or response == "y":
        print(
            "The cells are numberes 0-9 from top to bottom, left to right i.e. 1 would be the top left."
        )
        XorO = input("Would you like to go first? (Y/N):")
        if XorO == "Y" or XorO == "y":
            print("All right.")
            X = game.game_x()
            print(X)
        elif XorO == "N" or XorO == "n":
            print("Hah! Loser.")
            O = game.game_o()
            print(O)
