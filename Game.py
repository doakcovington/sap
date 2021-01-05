from Pawn import Pawn


class Game(Pawn):

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = [[' '] * 8] * 4

    def fill_board(self):
        self.board.insert(0, ['X'] * 8)
        self.board.insert(1, ['X'] * 8)
        self.board.append(['X'] * 8)
        self.board.append(['X'] * 8)

    def display_board(self):
        for row in self.board:
            print(row)


g1 = Game('Doak', 'Heidi')
pawn = Pawn()
pawn.display_pawns()
g1.fill_board()
g1.display_board()


