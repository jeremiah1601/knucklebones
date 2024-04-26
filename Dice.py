import random


class Dice:
    """
    this class is responsible for handling commmon dice operations such as
        - rolling a dice
        - displaying its output, though this will be added later
    """

    def __init__(self):
        pass

    @staticmethod
    def roll() -> int:
        return random.randint(1, 6)
