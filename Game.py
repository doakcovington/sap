from Pawn import Pawn


class Game(Pawn):

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = [[' '] * 8] * 4

    def start_game(self):
        if self.player1 and self.player2:
            print('Welcome to SAP')
            user_input = input('Enter Y to start a new game')
            if user_input.lower() == 'y':
                self.fill_board()
                self.display_board()
            else:
                print('SHUT IT DOWN')

    def fill_board(self):
        self.board.insert(0, ['X'] * 8)
        self.board.insert(1, ['X'] * 8)
        self.board.append(['X'] * 8)
        self.board.append(['X'] * 8)

    def display_board(self):
        for row in self.board:
            print(row)

    @staticmethod
    def start_game_message():
        print("Are you the smartest pawn?")


g1 = Game('Doak', 'Heidi')
pawn = Pawn()
g1.start_game_message()
g1.start_game()


