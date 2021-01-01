class Game:

    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
        self.board = [[""] * 8] * 8

    def display_board(self):
        for row in self.board:
            print(row)


g1 = Game('Doak', 'Heidi')
g1.display_board()