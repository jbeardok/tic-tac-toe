import random

board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

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

def show_board():
    for row in board:
        print(row)
    print()

def player_choice():
    human = input("Will you be X or O? ")
    human = human.upper()
    computer = ''
    print("You will be " + human)
    if human == 'X':
        computer = 'O'
    else:
        computer = 'X'
    return human, computer

def human_move(human, computer):
    row = int(input("Enter the row: "))
    column = int(input("Enter the cell (column): "))
    board[row][column] = human

def checkXWin():
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

def checkOWin():
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

def boardFull():
    full_cells = 0
    for row in board:
        for cell in row:
            if cell == 'X' or cell == 'O':
                full_cells += 1
    if full_cells == 9:
        return True

title()
show_board()
human, computer = player_choice()

xwin = False
owin = False
full = False

for i in range(9):
    if owin == True or xwin == True or full == True:
        break
    if human == 'X':
        human_move(human, computer)
        show_board()
        xwin = checkXWin()
        full = boardFull()
    else:
        human_move(human, computer)
        show_board()
        full = boardFull()

if owin == True:
    print("O Wins this game!")
elif xwin == True:
    print("X Wins this game!")
else:
    print("Draw!")
    
# def computer_move():
#     row = random.randint(0,3)
#     column = random.randint(0,3)
#     if board[row][column] == human:
#         row = random.randint(0,3)
#         column = random.randint(0,3)
        