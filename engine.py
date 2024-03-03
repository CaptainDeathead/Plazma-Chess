import copy
import utils

class Board:
    def __init__(self):
        self.board = [[10, 8, 9, 11, 12, 9, 8, 10],
                      [7, 7, 7, 7, 7, 7, 7, 7],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 2, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 1, 1, 1, 1, 1, 1, 1],
                      [4, 2, 3, 5, 6, 3, 2, 4]]
        
    def pieceAt(self, pos):
        if pos[0] < 0 or pos[0] > 7 or pos[1] < 0 or pos[1] > 7: return (False, 0)
        piece = self.board[pos[1]][pos[0]]
        if piece != 0: return (True, piece)
        else: return (False, 0)

class Engine:
    def __init__(self):
        self.TURN_STR = {0: "white", 1: "black"}
        self.board = Board()
        self.turn = 0

    def move(self, pos, newPos):
        if newPos in self.generateMoves(pos):
            self.board.board[newPos[1]][newPos[0]] = self.board.board[pos[1]][pos[0]]
            self.board.board[pos[1]][pos[0]] = 0
        else: raise Exception("Illegal move!")

    def __moveWithoutCheck(self, pos, newPos):
        self.board.board[newPos[1]][newPos[0]] = self.board.board[pos[1]][pos[0]]
        self.board.board[pos[1]][pos[0]] = 0

    def inCheck(self, turn):
        king = None
        for y in range(8):
            for x in range(8):
                if turn == 0 and self.board.board[y][x] == 6: king = (x, y)
                elif turn == 1 and self.board.board[y][x] == 12: king = (x, y)

        diagonal = self.generateDiagonalMoves(king)
        for pos in diagonal:
            piece = self.board.board[pos[1]][pos[0]]
            if (piece == 9 or piece == 11) and turn == 0: return True
            elif (piece == 3 or piece == 5) and turn == 1: return True

        sliding = self.generateSlidingMoves(king)
        for pos in sliding:
            piece = self.board.board[pos[1]][pos[0]]
            if (piece == 10 or piece == 11) and turn == 0: return True
            elif (piece == 4 or piece == 5) and turn == 1: return True

        # pawn
        if turn == 0:
            if self.board.pieceAt((king[0]-1, king[1]-1))[1] == 7: return True
            elif self.board.pieceAt((king[0]+1, king[1]-1))[1] == 7: return True
        else:
            if self.board.pieceAt((king[0]-1, king[1]+1))[1] == 1: return True
            elif self.board.pieceAt((king[0]+1, king[1]+1))[1] == 1: return True

        # knight
        if turn == 0:
            if self.board.pieceAt((king[0]-1, king[1]-2))[1] == 8: return True
            elif self.board.pieceAt((king[0]+1, king[1]-2))[1] == 8: return True
            elif self.board.pieceAt((king[0]+2, king[1]-1))[1] == 8: return True
            elif self.board.pieceAt((king[0]+2, king[1]+1))[1] == 8: return True
            elif self.board.pieceAt((king[0]+1, king[1]+2))[1] == 8: return True
            elif self.board.pieceAt((king[0]-1, king[1]+2))[1] == 8: return True
            elif self.board.pieceAt((king[0]-2, king[1]+1))[1] == 8: return True
            elif self.board.pieceAt((king[0]-2, king[1]-1))[1] == 8: return True
        elif turn == 1:
            if self.board.pieceAt((king[0]-1, king[1]-2))[1] == 2: return True
            elif self.board.pieceAt((king[0]+1, king[1]-2))[1] == 2: return True
            elif self.board.pieceAt((king[0]+2, king[1]-1))[1] == 2: return True
            elif self.board.pieceAt((king[0]+2, king[1]+1))[1] == 2: return True
            elif self.board.pieceAt((king[0]+1, king[1]+2))[1] == 2: return True
            elif self.board.pieceAt((king[0]-1, king[1]+2))[1] == 2: return True
            elif self.board.pieceAt((king[0]-2, king[1]+1))[1] == 2: return True
            elif self.board.pieceAt((king[0]-2, king[1]-1))[1] == 2: return True

        # king
        if turn == 0:
            for y in range(-1, 2):
                for x in range(-1, 2):
                    if self.board.pieceAt((king[0]+x, king[1]+y))[1] == 12: return True
        elif turn == 1:
            for y in range(-1, 2):
                for x in range(-1, 2):
                    if self.board.pieceAt((king[0]+x, king[1]+y))[1] == 6: return True

    def generatePawnMoves(self, pos):
        moves = []

        if self.turn == 0:
            if pos[1] == 6 and not self.board.pieceAt((pos[0], 4))[0]: moves.append((pos[0], 4)) # 2 spaces forward

            if pos[1] > 0:
                if not self.board.pieceAt((pos[0], pos[1]-1))[0]: moves.append((pos[0], pos[1]-1)) # 1 space forward
                
                if pos[0] > 0:
                    col = self.board.pieceAt((pos[0]-1, pos[1]-1))
                    if col[0] and col[1] > 6: moves.append((pos[0]-1, pos[1]-1)) # 1 capture forward-left
                if pos[0] < 7:
                    col = self.board.pieceAt((pos[0]+1, pos[1]-1))
                    if col[0] and col[1] > 6: moves.append((pos[0]+1, pos[1]-1)) # 1 capture forward-right
        else:
            if pos[1] == 1 and not self.board.pieceAt((pos[0], 3))[0]: moves.append((pos[0], 3)) # 2 spaces forward

            if pos[1] < 7:
                if not self.board.pieceAt((pos[0], pos[1]+1))[0]: moves.append((pos[0], pos[1]+1)) # 1 space forward
                
                if pos[0] > 0:
                    col = self.board.pieceAt((pos[0]-1, pos[1]+1))
                    if col[0] and col[1] < 7: moves.append((pos[0]-1, pos[1]+1)) # 1 capture forward-left
                if pos[0] < 7:
                    col = self.board.pieceAt((pos[0]+1, pos[1]+1))
                    if col[0] and col[1] < 7: moves.append((pos[0]+1, pos[1]+1)) # 1 capture forward-right
        
        return moves

    def generateKnightMoves(self, pos):
        moves = []

        moves.append((pos[0]-1, pos[1]-2))
        moves.append((pos[0]+1, pos[1]-2))
        moves.append((pos[0]+2, pos[1]-1))
        moves.append((pos[0]+2, pos[1]+1))
        moves.append((pos[0]+1, pos[1]+2))
        moves.append((pos[0]-1, pos[1]+2))
        moves.append((pos[0]-2, pos[1]+1))
        moves.append((pos[0]-2, pos[1]-1))

        newMoves = []
        for move in moves:
            if move[0] < 0 or move[0] > 7 or move[1] < 0 or move[1] > 7: continue
            
            piece = self.board.pieceAt(move)[1]
            if self.turn == 0 and piece > 6: newMoves.append(move)
            elif self.turn == 1 and piece < 7: newMoves.append(move)
            elif piece == 0: newMoves.append(move)
        
        return newMoves

    def generateSlidingMoves(self, pos):
        moves = []
        # forward
        for y in range(pos[1]-1, -1, -1):
            col = self.board.pieceAt((pos[0], y))
            if col[0]:
                if self.turn == 0 and col[1] > 6: moves.append((pos[0], y))
                elif self.turn == 1 and col[1] < 7: moves.append((pos[0], y))
                break
            else: moves.append((pos[0], y))

        # back
        for y in range(pos[1]+1, 8):
            col = self.board.pieceAt((pos[0], y))
            if col[0]:
                if self.turn == 0 and col[1] > 6: moves.append((pos[0], y))
                elif self.turn == 1 and col[1] < 7: moves.append((pos[0], y))
                break
            else: moves.append((pos[0], y))
            
        # left
        for x in range(pos[0]-1, -1, -1):
            col = self.board.pieceAt((x, pos[1]))
            if col[0]:
                if self.turn == 0 and col[1] > 6: moves.append((x, pos[1]))
                elif self.turn == 1 and col[1] < 7: moves.append((x, pos[1]))
                break
            else: moves.append((x, pos[1]))

        # right
        for x in range(pos[0]+1, 8):
            col = self.board.pieceAt((x, pos[1]))
            if col[0]:
                if self.turn == 0 and col[1] > 6: moves.append((x, pos[1]))
                elif self.turn == 1 and col[1] < 7: moves.append((x, pos[1]))
                break
            else: moves.append((x, pos[1]))

        return moves
    
    def generateDiagonalMoves(self, pos):
        moves = []
        # forward-left
        x = pos[0]
        y = pos[1]
        while True:
            x-=1
            y-=1
            if x < 0 or x > 7 or y < 0 or y > 7: break
            col = self.board.pieceAt((x, y))
            if col[0]:
                if self.turn == 0 and col[1] > 6: moves.append((x, y))
                elif self.turn == 1 and col[1] < 7: moves.append((x, y))
                break
            else: moves.append((x, y))
        # forward-right
        x = pos[0]
        y = pos[1]
        while True:
            x+=1
            y-=1
            if x < 0 or x > 7 or y < 0 or y > 7: break
            col = self.board.pieceAt((x, y))
            if col[0]:
                if self.turn == 0 and col[1] > 6: moves.append((x, y))
                elif self.turn == 1 and col[1] < 7: moves.append((x, y))
                break
            else: moves.append((x, y))
        # back-left
        x = pos[0]
        y = pos[1]
        while True:
            x-=1
            y+=1
            if x < 0 or x > 7 or y < 0 or y > 7: break
            col = self.board.pieceAt((x, y))
            if col[0]:
                if self.turn == 0 and col[1] > 6: moves.append((x, y))
                elif self.turn == 1 and col[1] < 7: moves.append((x, y))
                break
            else: moves.append((x, y))

        # back-right
        x = pos[0]
        y = pos[1]
        while True:
            x+=1
            y+=1
            if x < 0 or x > 7 or y < 0 or y > 7: break
            col = self.board.pieceAt((x, y))
            if col[0]:
                if self.turn == 0 and col[1] > 6: moves.append((x, y))
                elif self.turn == 1 and col[1] < 7: moves.append((x, y))
                break
            else: moves.append((x, y))

        return moves

    def generateMoves(self, pos):
        moves = []
        piece = self.board.board[pos[1]][pos[0]]

        if piece == 0: raise Exception(f"No valid piece found at ({pos[0]}, {pos[1]})!")

        elif piece == 1 or piece == 7: # pawn
            moves.extend(self.generatePawnMoves(pos))

        elif piece == 2 or piece == 8: # knight
            moves.extend(self.generateKnightMoves(pos))

        elif piece == 3 or piece == 9: # bishop
            moves.extend(self.generateDiagonalMoves(pos))

        elif piece == 4 or piece == 10: # rook
            moves.extend(self.generateSlidingMoves(pos))

        elif piece == 5 or piece == 11: # queen
            moves.extend(self.generateSlidingMoves(pos))
            moves.extend(self.generateDiagonalMoves(pos))

        elif piece == 6 or piece == 12: # king
            # forward
            if pos[1] > 0:
                # forward-left
                if pos[0] > 0:
                    col = self.board.pieceAt((pos[0]-1, pos[1]-1))
                    if col[0]:
                        if col[1] > 6: moves.append((pos[0]-1, pos[1]-1))
                    else: moves.append((pos[0]-1, pos[1]-1))
                
                # forward
                col = self.board.pieceAt((pos[0], pos[1]-1))
                if col[0]:
                    if col[1] > 6: moves.append((pos[0], pos[1]-1))
                else: moves.append((pos[0], pos[1]-1))

                # forward-right
                if pos[0] < 7:
                    col = self.board.pieceAt((pos[0]+1, pos[1]-1))
                    if col[0]:
                        if col[1] > 6: moves.append((pos[0]+1, pos[1]-1))
                    else: moves.append((pos[0]+1, pos[1]-1))

            # middle-left
            if pos[0] > 0:
                col = self.board.pieceAt((pos[0]-1, pos[1]))
                if col[0]:
                    if col[1] > 6: moves.append((pos[0]-1, pos[1]))
                else: moves.append((pos[0]-1, pos[1]))

            # middle-right
            if pos[0] < 7:
                col = self.board.pieceAt((pos[0]+1, pos[1]))
                if col[0]:
                    if col[1] > 6: moves.append((pos[0]+1, pos[1]))
                else: moves.append((pos[0]+1, pos[1]))

            # back
            if pos[1] < 7:
                # back-left
                if pos[0] > 0:
                    col = self.board.pieceAt((pos[0]-1, pos[1]+1))
                    if col[0]:
                        if col[1] > 6: moves.append((pos[0]-1, pos[1]+1))
                    else: moves.append((pos[0]-1, pos[1]+1))
                
                # back
                col = self.board.pieceAt((pos[0], pos[1]+1))
                if col[0]:
                    if col[1] > 6: moves.append((pos[0], pos[1]+1))
                else: moves.append((pos[0], pos[1]+1))

                # back-right
                if pos[0] < 7:
                    col = self.board.pieceAt((pos[0]+1, pos[1]+1))
                    if col[0]:
                        if col[1] > 6: moves.append((pos[0]+1, pos[1]+1))
                    else: moves.append((pos[0]+1, pos[1]+1))

        ogBoard = copy.deepcopy(self.board.board)

        newMoves = []
        for move in moves:
            self.__moveWithoutCheck(pos, move)
            if not self.inCheck(self.turn): newMoves.append(move)
            self.board.board = copy.deepcopy(ogBoard)
        
        moves = newMoves.copy()
        del newMoves

        return tuple(moves)