print('Player 1 is X and Player 2 is O')
user_fill = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ,' ']
i = 0

def check_win(board):
    check = False
    for i in range(0, 3):
        if board[3 * i + 1] == board[3 * i + 2] and board[3 * i + 2] == board[3 * i + 3] and board[3 * i + 3] != ' ':
            check = True
    for i in range(1, 4):
        if board[i + 0] == board[i + 3] and board[i + 3] == board[i + 6] and board[i + 6] != ' ':
            check = True
    if board[7] == board[5] and board[5] == board[3] and board[3] != ' ':
        check = True
    if board[1] == board[5] and board[5] == board[9] and board[9] != ' ':
        check = True
    return check

def display_board(board):
    print('   |   |   ')
    print(' {} | {} | {} '.format(board[7], board[8], board[9]))
    print('___|___|___')
    print('   |   |   ')
    print(' {} | {} | {} '.format(board[4], board[5], board[6]))
    print('___|___|___')
    print('   |   |   ')
    print(' {} | {} | {} '.format(board[1], board[2], board[3]))
    print('   |   |   ')


for i in range(1, 10):
    inp = int(input('Enter the position player : '))
    if i % 2 != 0:
        user_fill[inp] = 'X'
    else:
        user_fill[inp] = 'O'
    display_board(user_fill)
    if check_win(user_fill) == True:
        if i % 2 != 0:
            print('P1 is the Winner')
            break
        else:
            print('P2 is the Winner')
            break
    else:
        if i == 9:
            print('IT is A TIEEEE')
