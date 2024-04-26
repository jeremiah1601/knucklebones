from Board import Board
from Dice import Dice

class Knucklebones(Board, Dice):
    """
    this is the game engine class, it will be responsible for observing what
    happens to the two boards and returning game outcomes when appropriate
        - checks if columns have matching numbers
        - instructs the board to add and clean when appropriate
        - asks the player which column they want to put the dice
        - when board is full, returns the winner of the game
    """

    def __init__(self):
        # creates two boards, default names that can be changed later
        self.board_1 = Board("player 1")
        self.board_2 = Board("player 2")

    def play(self):
        """
        first gives the players the option to change their name, or not

        after this stage we start the game loop which has a few stages

            first decide whose turn it is, this is important when
            giving priority for dice deletion

            now the turn has been decided, roll the dice

            once the dice has been rolled, display the result and give the player a choice
            as to where they will place this dice

            if the board is full at this stage, end the game and decide the winner,
            continue otherwise

            once the dice has been placed, check if this causes the other board to
            have deletions

            once deletions have occurred, calculate the score and display it

            go to the next stage of the game loop
        """
        while True:
            # prompts the user with the options to change the players name, or not
            name_change = input("""do you want to input custom names?
            input 'Y' for yes
            input 'N' for no \n""")

            if name_change.upper() == 'Y':
                self.change_names()
                break
            elif name_change.upper() == 'N':
                print("skipping the name setting process...")
                break
            else:
                print("you did not enter a valid input, try again \n")
        """
        we will now start the game, we will be using a counter to keep track of turns since
        I like the way that it looks, this also means that I can set even numbers as player 2's
        turn and odd numbers as player 1's turn 
        """
        counter = 1
        board_full = False
        while not board_full:
            # decide whose turn it is
            if counter % 2 == 0:
                # player 2's turn
                self.player_rollNplace(self.board_2)
                #check for matches
                self.is_there_matching(priority_board=self.board_2,
                                       non_priority_board=self.board_1)
            else:
                # player 1's turn
                self.player_rollNplace(self.board_1)
                # check for matches
                self.is_there_matching(priority_board=self.board_1,
                                       non_priority_board=self.board_2)

            """
            now that we have added and deleted dice values where it is suitable, 
            we can now calculate and display scores
            """
            # calculating the score
            p1_score = self.score_board(board=self.board_1.get_board())
            p2_score = self.score_board(board=self.board_2.get_board())
            # displaying the board, alongside the scores
            print(f"{self.board_1.get_name()}\n{self.board_1.display_board()}\nscore: {p1_score}\n")

            print(f"{self.board_2.get_name()}\n{self.board_2.display_board()}\nscore: {p2_score}\n")

            board_full = self.board_1.board_full() or self.board_2.board_full()
            counter += 1

        if p1_score > p2_score:
            msg = f"{self.board_1.get_name} wins\n"
        elif p1_score < p2_score:
            msg = f"{self.board_2.get_name} wins\n"
        else:
            msg = "it's a draw\n"
        print(msg)


    def player_rollNplace(self, board: Board) -> None:
        """
        basically, rolls the dice and lets the player place the dice where they want
        """
        roll_cmd = input(f"hi {board.get_name()} enter anything to roll the dice\n")
        if roll_cmd:
            dice_val = self.roll()
            print()
        place_cmd = int(input(f"you rolled a {dice_val}, place this dice on a column with an empty space"
        "the addresses are 0, 1 and 2\n"))
        board.add_dice(place_cmd, dice_value=dice_val)
        return None

    def change_names(self) -> None:
        board_1.set_name(input("enter the name for player 1"))
        board_2.set_name(input("enter the name for player 2"))

    def score_board(self, board: list) -> int:
        counter = [{},
                   {},
                   {}]
        # lists the items in each column and notes down the frequency
        for i, column in enumerate(board):
            for row_item in column:
                if row_item in counter[i]:
                    counter[i][row_item] += 1
                else:
                    counter[i][row_item] = 1
        # calculates the score
        score = 0
        for column_tally in counter:
            for dice_num, freq in column_tally.items():
                score += dice_num * (freq ** 2)
        return score

    def is_there_matching(self, priority_board: Board, non_priority_board: Board) -> None:
        """
        Under the assumption that only one column will be deleted at a time,
        for each column on the board, check if there exists a matching number
        if there exists a match, delete from non priority board,
        """
        for i, (non_priority_column, priority_column) in enumerate(zip(non_priority_board.board, priority_board.board)):
            register = set()
            for item in priority_column:
                register.add(item)
            """
            now that we have completed our list of items in the priority board
            check if there exists a match in the non priority board, if there is 
            delete the matches and break our loop
            """
            for candidate_match in non_priority_column:
                if candidate_match in register:
                    non_priority_board.remove_value(i, candidate_match)
                    # non_priority_column.remove(candidate_match)
                    return None

        return None