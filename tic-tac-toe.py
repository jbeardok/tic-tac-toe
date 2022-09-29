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

title()
show_board()
human, computer = player_choice()

win = False
for i in range(9):
    if win == True:
        break
    else:
        human_move(human, computer)
        show_board()
        win = checkXWin()

print("X WINS THIS GAME!")

# def computer_move():
#     row = random.randint(0,3)
#     column = random.randint(0,3)
#     if board[row][column] == human:
#         row = random.randint(0,3)
#         column = random.randint(0,3)
        