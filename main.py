import colorama
from colorama import Fore, Back
class GameState():
    def __init__(self):
        # 8x8 2d list, each element has 2 characters
        # first character is color of piece w/b
        # second character is type of piece, K, Q, R, B, N, p
        # "--" is empty space with no piece
        # text based
        self.board = [
            [(Back.BLACK + "bR" + Back.RESET), (Back.BLACK + "bN" + Back.RESET), (Back.BLACK + "bB" + Back.RESET), (Back.BLACK + "bQ" + Back.RESET), (Back.BLACK + "bK" + Back.RESET), (Back.BLACK + "bB" + Back.RESET), (Back.BLACK + "bN" + Back.RESET), (Back.BLACK + "bR" + Back.RESET), (Back.CYAN + "| r0" + Back.RESET)],
            [(Back.BLACK + "bp" + Back.RESET), (Back.BLACK + "bp" + Back.RESET), (Back.BLACK + "bp" + Back.RESET), (Back.BLACK + "bp" + Back.RESET), (Back.BLACK + "bp" + Back.RESET), (Back.BLACK + "bp" + Back.RESET), (Back.BLACK + "bp" + Back.RESET), (Back.BLACK + "bp" + Back.RESET), (Back.CYAN + "| r1" + Back.RESET)],
            [(Back.CYAN + "--"), (Back.CYAN + "--"), (Back.CYAN + "--"), (Back.CYAN + "--"), (Back.CYAN + "--"), (Back.CYAN + "--"), (Back.CYAN + "--"), ("--" + Back.RESET), (Back.CYAN + "| r2" + Back.RESET)],
            [(Back.CYAN + "--"), (Back.CYAN + "--"), (Back.CYAN + "--"), (Back.CYAN + "--"), (Back.CYAN + "--"), (Back.CYAN + "--"), (Back.CYAN + "--"), ("--" + Back.RESET), (Back.CYAN + "| r3" + Back.RESET)],
            [(Back.CYAN + "--"), (Back.CYAN + "--"), (Back.CYAN + "--"), (Back.CYAN + "--"), (Back.CYAN + "--"), (Back.CYAN + "--"), (Back.CYAN + "--"), ("--" + Back.RESET), (Back.CYAN + "| r4" + Back.RESET)],
            [(Back.CYAN + "--"), (Back.CYAN + "--"), (Back.CYAN + "--"), (Back.CYAN + "--"), (Back.CYAN + "--"), (Back.CYAN + "--"), (Back.CYAN + "--"), ("--" + Back.RESET), (Back.CYAN + "| r5" + Back.RESET)],
            [(Back.WHITE + "wp" + Back.RESET), (Back.WHITE + "wp" + Back.RESET), (Back.WHITE + "wp" + Back.RESET), (Back.WHITE + "wp" + Back.RESET), (Back.WHITE + "wp" + Back.RESET), (Back.WHITE + "wp" + Back.RESET), (Back.WHITE + "wp" + Back.RESET), (Back.WHITE + "wp" + Back.RESET), (Back.CYAN + "| r6" + Back.RESET)],
            [(Back.WHITE + "wR" + Back.RESET), (Back.WHITE + "wN" + Back.RESET), (Back.WHITE + "wB" + Back.RESET), (Back.WHITE + "wQ" + Back.RESET), (Back.WHITE + "wK" + Back.RESET), (Back.WHITE + "wB" + Back.RESET), (Back.WHITE + "wN" + Back.RESET), (Back.WHITE + "wR" + Back.RESET), (Back.CYAN + "| r7" + Back.RESET)],
            ["__", "__", "__", "__", "__", "__", "__", "__"],
            [(Back.CYAN + "c0"), (Back.CYAN + "c1"), ("c2"), ("c3"), ("c4"), ("c5"), ("c6"), ("c7" + Back.RESET)]
        ]
        self.white_to_move = True

    def display_board(self):
        
        for row in self.board:
            print(Back.CYAN+" ".join(row)+Back.RESET)
        print(Back.RESET)

    def make_move(self, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        piece = self.board[start_row][start_col]

        if piece == "--":
            print("No piece at the starting position.")
            return False
        if (self.white_to_move and piece[0] =='b') or (not self.white_to_move and piece[0] == 'w'):
            print("It's not your turn.")       
            return False
        
        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = "--"
        self.white_to_move = not self.white_to_move
        return True

def get_position_input(prompt):
        while True:
            try:
                pos = input(prompt)
                row, col = map(int, pos.split())
                if 0 <= row < 8 and 0 <= col < 8:
                    return row, col
                else:
                    print("Position out of bounds.")
            except ValueError:
                print("Invalid input. Use format 'row col' (example: '1 2').")

def play_game():
    game = GameState()

    print("Welcome to Tomydas Chess!\n")

    while True:
        game.display_board()
        player = "White" if game.white_to_move else "Black"
        print(f"{player}'s turn")

        valid_move = False
        while not valid_move:
            print()
            print("Enter the start position. (example: '1 2' for row 1, column 2):")
            start_pos = get_position_input("Start position: ")
            print("Enter the end position. (example: '1 2' for row 1, column 2):")
            end_pos = get_position_input("End position: ")
            print()
            valid_move = game.make_move(start_pos, end_pos)
            if not valid_move:
                print("Invalid move. Try again.")

play_game()