import random

board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
title = '''
|///////////////////////////////////////////////////|
|### ### ###     ###   #    ###      ###  ###   ### |
| #   #  #        #   # #   #         #  #   #  #   | 
| #   #  #        #  #   #  #         #  #   #  ##  | 
| #   #  #        #  #####  #         #  #   #  #   | 
| #  ### ###      #  #   #  ###       #   ###   ### | 
|///////////////////////////////////////////////////|
'''
def show_board():
    print(title)
    for row in board:
        print(row)
    print()

human = input("Will you be X or O? ")
human = human.upper()
computer = ''
print("You will be " + human)

if human == 'X':
    computer == 'O'
    row = int(input("Enter the row: "))
    column = int(input("Enter the cell (column): "))
    board[row][column] = human
else:
    computer == 'X'
show_board()
