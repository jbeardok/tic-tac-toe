from random import *


class TicTacToe:
    def __init__(self):
        self.board = [['-'] * 3 for i in range(3)]
        self.n = len(self.board)

    def check_match(self, player_list):
        # Checks rows, cols, forward and back diagonals
        for player in player_list:
            for i in range(3):
                if self.board[i][0]==self.board[i][1]==self.board[i][2]==player or \
            self.board[0][i]==self.board[1][i]==self.board[2][i]==player or \
            self.board[0][0]==self.board[int(self.n/2)][int(self.n/2)]==self.board[self.n-1][self.n-1]==player or \
            self.board[self.n-1][0]==self.board[int(self.n/2)][int(self.n/2)]==self.board[0][self.n-1]==player:
                    return True
        return False

    def display_board(self):
        print()
        for r in self.board: print(r)

    def start(self):
        match = False
        # Game is over once 9 turns have passed with no match
        for x in range(9):
            self.display_board()
            # Begin round, player's turn
            player = True
            while player:
                # Player input
                if x % 2 == 0:
                    r = int(input('row: '))
                    c = int(input('column: '))
                    # Check if cell taken
                    if self.board[r][c] == '-':
                        self.board[r][c] = 'X'
                        # If not break while loop
                        player = False
                else:
                    r = randint(0, 2)
                    c = randint(0, 2)
                    if self.board[r][c] == '-':
                        self.board[r][c] = 'O'
                        player = False
            match = self.check_match(['X', 'O'])
            if match: print('win'); break
            else: print('no match')
        if not match: print('board is full')


game = TicTacToe()
game.start()
