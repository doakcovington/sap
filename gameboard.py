class GameBoard:

    def __init__(self):
        self.board = [[''] * 8] * 8

    def print_board(self):
        print(self.board)
g1 = GameBoard()
g1.print_board()