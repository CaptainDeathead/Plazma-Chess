import chess
import pygame
import os

board = chess.Board()

pieces_sprites = [
    "Sprites/white pawn.png",
    "Sprites/white knight.png",
    "Sprites/white bishop.png",
    "Sprites/white rook.png",
    "Sprites/white queen.png",
    "Sprites/white king.png",
    "Sprites/black pawn.png",
    "Sprites/black knight.png",
    "Sprites/black bishop.png",
    "Sprites/black rook.png",
    "Sprites/black queen.png",
    "Sprites/black king.png"
]

move_dot = pygame.image.load("Sprites/Moves Circle.png")
selected_piece = None

ai_move_piece = 00
ai_move = 00

def change_ai_move(new_ai_move_piece, new_ai_move):
    global ai_move_piece
    global ai_move
    ai_move_piece = new_ai_move_piece
    ai_move = new_ai_move

# load the pieces sprites
pieces = []
for i in range(len(pieces_sprites)):
    pieces.append(pygame.image.load(pieces_sprites[i]))

# show the board using pygame
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Chess")
screen.fill((255, 255, 255))

# draw the board
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            # red
            pygame.draw.rect(screen, (255, 0, 0), (i * 100, j * 100, 100, 100))
        else:
            # white
            pygame.draw.rect(screen, (255, 255, 255), (i * 100, j * 100, 100, 100))

def draw_pieces():
    # draw the pieces
    for i in range(8):
        for j in range(8):
            piece = board.piece_at(i + j * 8)
            if piece is not None:
                if piece.color:
                    # white
                    if piece.piece_type == 1:
                        screen.blit(pieces[0], (i * 100, j * 100))
                    elif piece.piece_type == 2:
                        screen.blit(pieces[1], (i * 100, j * 100))
                    elif piece.piece_type == 3:
                        screen.blit(pieces[2], (i * 100, j * 100))
                    elif piece.piece_type == 4:
                        screen.blit(pieces[3], (i * 100, j * 100))
                    elif piece.piece_type == 5:
                        screen.blit(pieces[4], (i * 100, j * 100))
                    elif piece.piece_type == 6:
                        screen.blit(pieces[5], (i * 100, j * 100))
                else:
                    # black
                    if piece.piece_type == 1:
                        screen.blit(pieces[6], (i * 100, j * 100))
                    elif piece.piece_type == 2:
                        screen.blit(pieces[7], (i * 100, j * 100))
                    elif piece.piece_type == 3:
                        screen.blit(pieces[8], (i * 100, j * 100))
                    elif piece.piece_type == 4:
                        screen.blit(pieces[9], (i * 100, j * 100))
                    elif piece.piece_type == 5:
                        screen.blit(pieces[10], (i * 100, j * 100))
                    elif piece.piece_type == 6:
                        screen.blit(pieces[11], (i * 100, j * 100))
draw_pieces()
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # check for checkmate
        if board.is_checkmate():
            print("Checkmate! " + str(board.turn) + " lost the game!")
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            # check if the mouse is on a piece
            for i in range(8):
                for j in range(8):
                    piece = board.piece_at(i + j * 8)
                    if piece is not None:
                        if pos[0] >= i * 100 and pos[0] <= (i + 1) * 100 and pos[1] >= j * 100 and pos[1] <= (j + 1) * 100:
                            # show the possible moves for the piece
                            for move in board.legal_moves:
                                if move.from_square == i + j * 8:
                                    screen.blit(move_dot, ((move.to_square % 8) * 100, (move.to_square // 8) * 100))
                                    selected_piece = (i, j)
                                    print(selected_piece)
                                    pygame.display.update()

            # check if the mouse is on a move
            for move in board.legal_moves:
                # check if the mouse is on a valid move according to the selected piece
                if selected_piece is not None:
                    if move.from_square == selected_piece[0] + selected_piece[1] * 8:
                        if pos[0] >= (move.to_square % 8) * 100 and pos[0] <= ((move.to_square % 8) + 1) * 100 and pos[1] >= (move.to_square // 8) * 100 and pos[1] <= ((move.to_square // 8) + 1) * 100:
                            try:
                                board.push(move)
                                # draw the board without any pieces
                                for i in range(8):
                                    for j in range(8):
                                        if (i + j) % 2 == 0:
                                            # red
                                            pygame.draw.rect(screen, (255, 0, 0), (i * 100, j * 100, 100, 100))
                                        else:
                                            # white
                                            pygame.draw.rect(screen, (255, 255, 255), (i * 100, j * 100, 100, 100))
                                draw_pieces()
                            except:
                                print("Invalid move!")
    
            # check if a pawn can be promoted
            if board.is_queenside_castling(move):
                print("Promote to queen")
                # make the pawn a queen
                board.set_piece_at(move.to_square, chess.Queen(board.turn))
                # draw the board without any pieces
                for i in range(8):
                    for j in range(8):
                        if (i + j) % 2 == 0:
                            # red
                            pygame.draw.rect(screen, (255, 0, 0), (i * 100, j * 100, 100, 100))
                        else:
                            # white
                            pygame.draw.rect(screen, (255, 255, 255), (i * 100, j * 100, 100, 100))
                draw_pieces()

        if ai_move_piece != 00:
            if ai_move != 00:
                # translate the ai_move_piece and ai_move to a [x, y] position
                ai_move_piece_x = ai_move_piece % 8
                ai_move_piece_y = ai_move_piece // 8
                ai_move_x = ai_move % 8
                ai_move_y = ai_move // 8
                # move the piece on the board
                board.push(chess.Move(ai_move_piece, ai_move))
                # draw the board without any pieces
                for i in range(8):
                    for j in range(8):
                        if (i + j) % 2 == 0:
                            # red
                            pygame.draw.rect(screen, (255, 0, 0), (i * 100, j * 100, 100, 100))
                        else:
                            # white
                            pygame.draw.rect(screen, (255, 255, 255), (i * 100, j * 100, 100, 100))
                draw_pieces()
            
                # reset the ai_move_piece and ai_move
                ai_move_piece = 00
                ai_move = 00
                pygame.display.update()

    pygame.time.delay(100)
    pygame.display.update()
