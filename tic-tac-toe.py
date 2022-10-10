import random

def title():
    banner = '''
    |///////////////////////////////////////////////////|
    |### ### ###     ###   #    ###      ###  ###   ### |
    | #   #  #        #   # #   #         #  #   #  #   | 
    | #   #  #        #  #   #  #         #  #   #  ##  | 
    | #   #  #        #  #####  #         #  #   #  #   | 
    | #  ### ###      #  #   #  ###       #   ###   ### | 
    |///////////////////////////////////////////////////|
    '''
    print(banner)
    print("Choose values between 0-2.\nFor rows: 0 = top, 1 = middle, 2 = bottom\nFor columns: 0 = left, 1 = middle, 2 = right\n")

def show_board(board):
    for row in board:
        print(row)
    print()

def player_choice():
    num_players = int(input("1 or 2 player game? Enter a number: "))
    player1 = input("Will you be X or O? ")
    player1 = player1.upper()
    player2 = ''
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    print("Player 1 will be " + player1 + ", player 2 will be " + player2 + ".")
    return num_players, player1, player2

def human_move(board, human):
    row = int(input("Enter the row: "))
    column = int(input("Enter the cell (column): "))
    if row < 0  or row > 2:
        row = int(input("Row: Number is out of range. Enter an integer 0-2: "))
    if column < 0 or column > 2:
        column = int(input("Cell (Column): Number is out of range. Enter an integer 0-2: "))
    while board[row][column] != '-':
        row = int(input("Cell is taken. Enter the row: "))
        column = int(input("Enter the cell (column): "))
    board[row][column] = human

def computer_move(board, computer):
    row = random.randint(0,2)
    column = random.randint(0,2)
    while board[row][column] != '-':
        row = random.randint(0,2)
        column = random.randint(0,2)
    board[row][column] = computer

def checkXWin(board):
    for row in range(3):
        if board[row][0] == 'X' and board[row][1] == 'X' and board[row][2] == 'X':
            return True
        else:
            continue
    for column in range(3):
        if board[0][column] == 'X' and board[1][column] == 'X' and board[2][column] == 'X':
            return True
        else:
            continue
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        return True
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        return True
    else:
        return False

def checkOWin(board):
    for row in range(3):
        if board[row][0] == 'O' and board[row][1] == 'O' and board[row][2] == 'O':
            return True
        else:
            continue
    for column in range(3):
        if board[0][column] == 'O' and board[1][column] == 'O' and board[2][column] == 'O':
            return True
        else:
            continue
    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        return True
    elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        return True
    else:
        return False

def boardFull(board):
    full_cells = 0
    for row in board:
        for cell in row:
            if cell == 'X' or cell == 'O':
                full_cells += 1
    if full_cells == 9:
        return True

def main():
    board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    title()
    num_players, player1, player2 = player_choice()
    show_board(board)

    xwin = False
    owin = False
    fullboard = False
    # Player1 is a human, player2 is random
    if num_players == 1:
        while owin != True or xwin != True or fullboard != True:
            if player1 == 'X':
                # IF PLAYER IS X, COMPUTER IS O
                human_move(board, player1)
                show_board(board)
                xwin = checkXWin(board)
                fullboard = boardFull(board)
                if xwin == True or fullboard == True:
                    break
                computer_move(board, player2)
                show_board(board)
                owin = checkOWin(board)
                fullboard = boardFull(board)
                if owin == True or fullboard ==True:
                    break
            else:
                # IF PLAYER IS O, COMPUTER IS X
                computer_move(board, player2)
                show_board(board)
                xwin = checkXWin(board)
                fullboard = boardFull(board)
                if xwin == True or fullboard == True:
                    break
                human_move(board, player1)
                show_board(board)
                owin = checkOWin(board)
                fullboard = boardFull(board)
                if owin == True or fullboard == True:
                    break
    else:
        # Both players are human
        while owin != True or xwin != True or fullboard != True:
            if player1 == 'X':
                # IF PLAYER1 IS X, Player2 IS O
                print("Player 1's turn!")
                human_move(board, player1)
                show_board(board)
                xwin = checkXWin(board)
                fullboard = boardFull(board)
                if xwin == True or fullboard == True:
                    break
                print("Player 2's turn!")
                human_move(board, player2)
                show_board(board)
                owin = checkOWin(board)
                fullboard = boardFull(board)
                if owin == True or fullboard ==True:
                    break
            else:
                # IF PLAYER IS O, COMPUTER IS X
                print("Player 2's turn!")
                human_move(board, player2)
                show_board(board)
                xwin = checkXWin(board)
                fullboard = boardFull(board)
                if xwin == True or fullboard == True:
                    break
                print("Player 1's turn!")
                human_move(board, player1)
                show_board(board)
                owin = checkOWin(board)
                fullboard = boardFull(board)
                if owin == True or fullboard == True:
                    break
        
    if owin == True:
        print("O Wins this game!")
    elif xwin == True:
        print("X Wins this game!")
    else:
        print("Draw!")

main()