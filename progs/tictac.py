theBoard = {
    'top-l': ' ',
    'top-m': ' ',
    'top-r': ' ',
    'mid-l': ' ',
    'mid-m': ' ',
    'mid-r': ' ',
    'low-l': ' ',
    'low-m': ' ',
    'low-r': ' ',
}


def printBoard(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-+-+-')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-+-+-')
    print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])


turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('turn for ' + turn + ' type your move :')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)