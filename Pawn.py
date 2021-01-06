
class Pawn:

    def __init__(self):
        self.player1_pawns = ['W'] * 16
        self.player2_pawns = ["E"] * 16

    def display_pawns(self):
        print('Player 1 Pawns:')
        print(self.player1_pawns)
        print('Player 2 Pawns:')
        print(self.player2_pawns)


