from Knucklebones import Knucklebones

"""
this is a recreation of the game knucklebones from the game, cult of the lamb
the game requires 2 players and provides each of them to have a 3x3 board each
the rules are provided in game as follows:
    1. when dice of the same number are placed on the same column, their score is multiplied

    2. destroy your opponents dice by matching your dice to theirs

the game ends when one player has completely filled their board, the player with the
most points will win the game
"""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = Knucklebones()
    game.play()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
