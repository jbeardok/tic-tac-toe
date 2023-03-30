from random import *
board = [['-'] * 3 for i in range(3)]
for r in board:
    print(r)
# board = [['-', '-', '-'],
#          ['-', '-', '-'],
#          ['-', '-', '-']]
n = len(board)
match = False
# Game is over once 9 turns have passed with no match
for x in range(9):
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
    # Display board in terminal
    print()
    for r in board:
        print(r)
    # Check for a match
    # rows, cols, diags
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]=='X' or \
        board[0][i]==board[1][i]==board[2][i]=='X' or \
        board[0][0]==board[int(n/2)][int(n/2)]==board[n-1][n-1]=='X' or \
        board[n-1][0]==board[int(n/2)][int(n/2)]==board[0][n-1]=='X':
            # if match is found, break game loop
            match = True
        if board[i][0]==board[i][1]==board[i][2]=='O' or \
        board[0][i]==board[1][i]==board[2][i]=='O' or \
        board[0][0]==board[int(n/2)][int(n/2)]==board[n-1][n-1]=='O' or \
        board[n-1][0]==board[int(n/2)][int(n/2)]==board[0][n-1]=='O':
            match = True
    if match:
        print('win')
        break
if not match:
    print('board full')               