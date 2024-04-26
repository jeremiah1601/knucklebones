import typing

class Board:
    """
    this class will be responsible for the dice on a players board
        - removing columns when instructed to
        - adding dice when instructed to
        - notifying the game engine when the board is full
    """

    """
    we will be using a 3x3 board, but our board list will still be 2-dimensional with the following
    naming convention: 
        0,0   1,0   2,0
        0,1   1,1   2,1
        0,2   1,2   2,2
    so that we can wipe columns easily 
    """
    def __init__(self, player_name: str):
        # generates an empty board
        self.board = [[],
                      [],
                      []]
        # sets their name
        self.name = player_name

    def get_board(self):
        return self.board

    def set_name(self, player_name: str) -> None:
        self.name = player_name

    def get_name(self):
        return self.name

    def add_dice(self, column: int, dice_value: int) -> None:
        # if our board is now full, notify the game engine
        self.board[column].append(dice_value)

    def board_full(self) -> bool:
        i = 0
        for column in self.board:
            for row_item in column:
                i += 1
        if i == 9:
            return True
        else:
            return False

    def remove_value(self, column: int, value: int) -> None:
        for i, item in enumerate(self.board[column]):
            if item == value:
                del self.board[column][i]

    def display_board(self) -> str:
        # displays the boards values
        # if there is no value, we display a zero
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(9):
            try:
                board[i // 3][i % 3] = self.board[i // 3][i % 3]
            except IndexError:
                continue
        message = f"{board[0][0]} | {board[1][0]} | {board[2][0]}\n------------\n{board[0][1]} | {board[1][1]} | {board[2][1]}\n____________\n{board[0][2]} | {board[1][2]} | {board[2][2]}"
        return message

