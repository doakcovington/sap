class Pawn:

    def __init__(self):
        self.player1_pawns = ['W'] * 16
        self.player2_pawns = ["E"] * 16

    def display_pawns(self):
        print(self.player1_pawns)
        print(self.player2_pawns)


a = Pawn()
a.display_pawns()
