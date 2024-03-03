PIECE_UNICODES = {0: ' ', 1: '♟︎', 2: '♞', 3: '♝', 4: '♜', 5: '♛', 6: '♚', 7: '♟︎', 8: '♞', 9: '♝', 10: '♜', 11: '♛', 12: '♚'}

ESC = '\x1b'
WHITE_BG  = ESC + '[47m'
BLACK_BG  = ESC + '[40m'
RED_BG    = ESC + '[41m'
YELLOW_BG = ESC + '[43m'
GREEN_BG  = ESC + '[42m'
BLUE_BG   = ESC + '[44m'
PURPLE_BG = ESC + '[45m'

def showState(board):
    printString = ""
    white = False
    for y in range(8):
        white = not white
        for x in range(8):
            if white: printString += WHITE_BG + PIECE_UNICODES[board[y][x]] + ' '
            else: printString += BLACK_BG + PIECE_UNICODES[board[y][x]] + ' '
            white = not white
        printString += BLACK_BG
        printString += '\n'
    return printString