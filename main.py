from random import *

def check_match(player_list):
    # Checks rows, cols, forward and back diags
    for player in player_list:
        for i in range(3):
            if board[i][0]==board[i][1]==board[i][2]==player or \
        board[0][i]==board[1][i]==board[2][i]==player or \
        board[0][0]==board[int(n/2)][int(n/2)]==board[n-1][n-1]==player or \
        board[n-1][0]==board[int(n/2)][int(n/2)]==board[0][n-1]==player:
                return True
    return False

def display_board():
    print()
    for r in board:
        print(r)

board = [['-'] * 3 for i in range(3)]
n = len(board)

match = False
# Game is over once 9 turns have passed with no match
for x in range(9):
    display_board()
    # Begin round, player's turn
    player = True
    while player:
        # Player input
        if x % 2 == 0: 
            r = int(input('row: ')) 
            c = int(input('column: '))
            # Check if cell taken
            if board[r][c] == '-':
                board[r][c] = 'X'
                # If not break while loop
                player = False
        else: 
            r = randint(0, 2)
            c = randint(0, 2)
            if board[r][c] == '-':
                board[r][c] = 'O' 
                player = False

    match = check_match(['X', 'O'])
    if match:
        print('win')
        break
if not match:
    print('board is full')               