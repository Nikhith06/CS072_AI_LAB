
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('\n')

def spaceFree(pos):
    return board[pos] == ' '

def checkWin():
    # Check rows, columns, and diagonals for a win
    if (board[1] == board[2] == board[3] != ' ' or
        board[4] == board[5] == board[6] != ' ' or
        board[7] == board[8] == board[9] != ' ' or
        board[1] == board[4] == board[7] != ' ' or
        board[2] == board[5] == board[8] != ' ' or
        board[3] == board[6] == board[9] != ' ' or
        board[1] == board[5] == board[9] != ' ' or
        board[3] == board[5] == board[7] != ' '):
        return True
    return False

def checkMoveForWin(move):
    # Check rows, columns, and diagonals for a specific move to win
    if (board[1] == board[2] == board[3] == move or
        board[4] == board[5] == board[6] == move or
        board[7] == board[8] == board[9] == move or
        board[1] == board[5] == board[9] == move or
        board[3] == board[5] == board[7] == move or
        board[1] == board[4] == board[7] == move or
        board[2] == board[5] == board[8] == move or
        board[3] == board[6] == board[9] == move):
        return True
    return False

def checkDraw():
    # Return True if all positions are filled, otherwise False
    return all(space != ' ' for space in board.values())

def insertLetter(letter, position):
    if spaceFree(position):
        board[position] = letter
        printBoard(board)

        if checkDraw():
            print('Draw!')
            exit()
        elif checkWin():
            if letter == 'X':
                print('Bot wins!')
            else:
                print('You win!')
            exit()
    else:
        print('Position taken, please pick a different position.')
        position = int(input('Enter new position: '))
        insertLetter(letter, position)

def playerMove():
    position = int(input('Enter position for O: '))
    insertLetter('O', position)

def compMove():
    bestScore = -1000
    bestMove = 0

    for key in board.keys():
        if spaceFree(key):
            board[key] = 'X'
            score = minimax(board, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key

    insertLetter('X', bestMove)

def minimax(board, isMaximizing):
    if checkMoveForWin('X'):
        return 1
    elif checkMoveForWin('O'):
        return -1
    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = -1000
        for key in board.keys():
            if spaceFree(key):
                board[key] = 'X'
                score = minimax(board, False)
                board[key] = ' '
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 1000
        for key in board.keys():
            if spaceFree(key):
                board[key] = 'O'
                score = minimax(board, True)
                board[key] = ' '
                bestScore = min(score, bestScore)
        return bestScore

while not checkWin() and not checkDraw():
    compMove()
    playerMove()
