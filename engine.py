import chess
import random
import threading

def process(board):
    # get all legal moves
    legal_moves = list(board.legal_moves)
    # choose a random move
    move = random.choice(legal_moves)
    # return the move
    return move