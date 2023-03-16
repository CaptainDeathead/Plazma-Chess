import pygame
import sys

pygame.init()

selected_piece = None

# set the screen size
screen = pygame.display.set_mode((800, 800))

# set the title of the screen
pygame.display.set_caption("Chess")

# set the background color
screen.fill((255, 255, 255))

# set the color of the grid
black = (0, 0, 0)
white = (255, 255, 255)

# set the width and height of the grid
width = 100
height = 100

# set the margin between each cell
margin = 1

# make a grid of 8x8
grid = [[0 for x in range(8)] for y in range(8)]

# draw the grid
for row in range(8):
    for column in range(8):
        if (row + column) % 2 == 0:
            color = white
        else:
            color = black
        pygame.draw.rect(screen, color, [(margin + width) * column + margin, (margin + height) * row + margin, width, height])

# preload the sprites
sprites = {
    "WhiteRook": pygame.image.load("Sprites/White Rook.png"),
    "WhiteKnight": pygame.image.load("Sprites/White Knight.png"),
    "WhiteBishop": pygame.image.load("Sprites/White Bishop.png"),
    "WhiteQueen": pygame.image.load("Sprites/White Queen.png"),
    "WhiteKing": pygame.image.load("Sprites/White King.png"),
    "WhitePawn": pygame.image.load("Sprites/White Pawn.png"),
    "BlackRook": pygame.image.load("Sprites/Black Rook.png"),
    "BlackKnight": pygame.image.load("Sprites/Black Knight.png"),
    "BlackBishop": pygame.image.load("Sprites/Black Bishop.png"),
    "BlackQueen": pygame.image.load("Sprites/Black Queen.png"),
    "BlackKing": pygame.image.load("Sprites/Black King.png"),
    "BlackPawn": pygame.image.load("Sprites/Black Pawn.png"),
    "GreenSquare": pygame.image.load("Sprites/Moves Circle.png")
}

def check_moves(piece, row, column, selected_piece, grid):
    if piece == "WhitePawn":
        if row == 6:
            for move in white_pawn_moves:
                try:
                    if grid[row + move[0]][column + move[1]] == 0:
                        screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                        # add the GreenSquare to the grid
                        grid[row + move[0]][column + move[1]] = "GreenSquare"
                        selected_piece = row, column
                    elif "Black" in grid[row + white_pawn_kill_moves[0][0]][column + white_pawn_kill_moves[0][1]] and "Black" in grid[row + white_pawn_kill_moves[1][0]][column + white_pawn_kill_moves[1][1]]:
                        pygame.draw.rect(screen, (0, 255, 0), ((column + white_pawn_kill_moves[0][1]) * 100, (row + white_pawn_kill_moves[0][0]) * 100, 100, 100))
                        pygame.draw.rect(screen, (0, 255, 0), ((column + white_pawn_kill_moves[1][1]) * 100, (row + white_pawn_kill_moves[1][0]) * 100, 100, 100))
                        selected_piece = row, column
                    elif "Black" in grid[row + white_pawn_kill_moves[0][0]][column + white_pawn_kill_moves[0][1]]:
                        pygame.draw.rect(screen, (0, 255, 0), ((column + white_pawn_kill_moves[0][1]) * 100, (row + white_pawn_kill_moves[0][0]) * 100, 100, 100))
                        selected_piece = row, column
                    elif "Black" in grid[row + white_pawn_kill_moves[1][0]][column + white_pawn_kill_moves[1][1]]:
                        pygame.draw.rect(screen, (0, 255, 0), ((column + white_pawn_kill_moves[1][1]) * 100, (row + white_pawn_kill_moves[1][0]) * 100, 100, 100))
                        selected_piece = row, column
                    else:
                        continue
                except IndexError:
                    continue   
        else:
            for move in white_pawn_moves_1:
                try:
                    if grid[row + move[0]][column + move[1]] == 0:
                        screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                        # add the GreenSquare to the grid
                        grid[row + move[0]][column + move[1]] = "GreenSquare"
                        selected_piece = row, column
                    elif "Black" in grid[row + white_pawn_kill_moves[0][0]][column + white_pawn_kill_moves[0][1]] and "Black" in grid[row + white_pawn_kill_moves[1][0]][column + white_pawn_kill_moves[1][1]]:
                        pygame.draw.rect(screen, (0, 255, 0), ((column + white_pawn_kill_moves[0][1]) * 100, (row + white_pawn_kill_moves[0][0]) * 100, 100, 100))
                        pygame.draw.rect(screen, (0, 255, 0), ((column + white_pawn_kill_moves[1][1]) * 100, (row + white_pawn_kill_moves[1][0]) * 100, 100, 100))
                        selected_piece = row, column
                    elif "Black" in grid[row + white_pawn_kill_moves[0][0]][column + white_pawn_kill_moves[0][1]]:
                        pygame.draw.rect(screen, (0, 255, 0), ((column + white_pawn_kill_moves[0][1]) * 100, (row + white_pawn_kill_moves[0][0]) * 100, 100, 100))
                        selected_piece = row, column
                    elif "Black" in grid[row + white_pawn_kill_moves[1][0]][column + white_pawn_kill_moves[1][1]]:
                        pygame.draw.rect(screen, (0, 255, 0), ((column + white_pawn_kill_moves[1][1]) * 100, (row + white_pawn_kill_moves[1][0]) * 100, 100, 100))
                        selected_piece = row, column
                    else:
                        continue
                except IndexError:
                    continue

    elif piece == "BlackPawn":
        if row == 1:
            for move in black_pawn_moves:
                try:
                    if grid[row + move[0]][column + move[1]] == 0:
                        screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                        # add the GreenSquare to the grid
                        grid[row + move[0]][column + move[1]] = "GreenSquare"
                        selected_piece = row, column
                    elif "White" in grid[row + black_pawn_kill_moves[0][0]][column + black_pawn_kill_moves[0][1]] and "White" in grid[row + black_pawn_kill_moves[1][0]][column + black_pawn_kill_moves[1][1]]:
                        pygame.draw.rect(screen, (0, 255, 0), ((column + black_pawn_kill_moves[0][1]) * 100, (row + black_pawn_kill_moves[0][0]) * 100, 100, 100))
                        pygame.draw.rect(screen, (0, 255, 0), ((column + black_pawn_kill_moves[1][1]) * 100, (row + black_pawn_kill_moves[1][0]) * 100, 100, 100))
                        selected_piece = row, column
                    elif "White" in grid[row + black_pawn_kill_moves[0][0]][column + black_pawn_kill_moves[0][1]]:
                        pygame.draw.rect(screen, (0, 255, 0), ((column + black_pawn_kill_moves[0][1]) * 100, (row + black_pawn_kill_moves[0][0]) * 100, 100, 100))
                        selected_piece = row, column
                    elif "White" in grid[row + black_pawn_kill_moves[1][0]][column + black_pawn_kill_moves[1][1]]:
                        pygame.draw.rect(screen, (0, 255, 0), ((column + black_pawn_kill_moves[1][1]) * 100, (row + black_pawn_kill_moves[1][0]) * 100, 100, 100))
                        selected_piece = row, column
                    else:
                        continue
                except IndexError:
                    continue
        else:
            for move in black_pawn_moves_1:
                try:
                    if grid[row + move[0]][column + move[1]] == 0:
                        screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                        # add the GreenSquare to the grid
                        grid[row + move[0]][column + move[1]] = "GreenSquare"
                        selected_piece = row, column
                    elif "White" in grid[row + black_pawn_kill_moves[0][0]][column + black_pawn_kill_moves[0][1]] and "White" in grid[row + black_pawn_kill_moves[1][0]][column + black_pawn_kill_moves[1][1]]:
                        pygame.draw.rect(screen, (0, 255, 0), ((column + black_pawn_kill_moves[0][1]) * 100, (row + black_pawn_kill_moves[0][0]) * 100, 100, 100))
                        pygame.draw.rect(screen, (0, 255, 0), ((column + black_pawn_kill_moves[1][1]) * 100, (row + black_pawn_kill_moves[1][0]) * 100, 100, 100))
                        selected_piece = row, column
                    elif "White" in grid[row + black_pawn_kill_moves[0][0]][column + black_pawn_kill_moves[0][1]]:
                        pygame.draw.rect(screen, (0, 255, 0), ((column + black_pawn_kill_moves[0][1]) * 100, (row + black_pawn_kill_moves[0][0]) * 100, 100, 100))
                        selected_piece = row, column
                    elif "White" in grid[row + black_pawn_kill_moves[1][0]][column + black_pawn_kill_moves[1][1]]:
                        pygame.draw.rect(screen, (0, 255, 0), ((column + black_pawn_kill_moves[1][1]) * 100, (row + black_pawn_kill_moves[1][0]) * 100, 100, 100))
                        selected_piece = row, column
                    else:
                        continue
                except IndexError:
                    continue

    elif piece == "WhiteRook":
        for move in up_verticle_rook_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "Black" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in down_verticle_rook_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "Black" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in left_horizontal_rook_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "Black" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in right_horizontal_rook_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "Black" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
    elif piece == "BlackRook":
        for move in up_verticle_rook_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "White" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in down_verticle_rook_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "White" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in left_horizontal_rook_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "White" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in right_horizontal_rook_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "White" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
    elif piece == "WhiteKnight":
        for move in knight_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
            except IndexError:
                continue
    elif piece == "BlackKnight":
        for move in knight_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
            except IndexError:
                continue
    elif piece == "WhiteBishop":
        for move in up_left_bishop_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "Black" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in up_right_bishop_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "Black" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in down_left_bishop_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "Black" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in down_right_bishop_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "Black" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
    elif piece == "BlackBishop":
        for move in up_left_bishop_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "White" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in up_right_bishop_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "White" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in down_left_bishop_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "White" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in down_right_bishop_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "White" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
    elif piece == "WhiteQueen":
        for move in up_left_queen_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "Black" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in up_right_queen_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "Black" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in down_left_queen_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "Black" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in down_right_queen_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "Black" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in up_verticle_queen_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "Black" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in down_verticle_queen_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "Black" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in left_horizontal_queen_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "Black" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in right_horizontal_queen_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "Black" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
    elif piece == "BlackQueen":
        for move in up_left_queen_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "White" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in up_right_queen_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "White" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in down_left_queen_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "White" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in down_right_queen_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "White" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in up_verticle_queen_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "White" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in down_verticle_queen_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "White" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in left_horizontal_queen_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "White" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
        for move in right_horizontal_queen_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
                elif "White" in grid[row + move[0]][column + move[1]]:
                    # draw a green square
                    pygame.draw.rect(screen, (0, 255, 0), ((column + move[1]) * 100, (row + move[0]) * 100, 100, 100))
                    selected_piece = row, column
                    break
                else:
                    break
            except IndexError:
                break
    elif piece == "WhiteKing":
        for move in king_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
            except IndexError:
                continue
    elif piece == "BlackKing":
        for move in king_moves:
            try:
                if grid[row + move[0]][column + move[1]] == 0:
                    screen.blit(sprites["GreenSquare"], ((column + move[1]) * 100, (row + move[0]) * 100))
                    # add the GreenSquare to the grid
                    grid[row + move[0]][column + move[1]] = "GreenSquare"
                    selected_piece = row, column
            except IndexError:
                continue

    else:
        if piece == "GreenSquare":
            # move the piece to the GreenSquare
            grid[row][column] = grid[selected_piece[0]][selected_piece[1]]
            grid[selected_piece[0]][selected_piece[1]] = 0

            # reset the selected piece
            selected_piece = None

            # reset the GreenSquares
            for row in range(8):
                for column in range(8):
                    if grid[row][column] == "GreenSquare":
                        grid[row][column] = 0

            for i in range(8):
                print(grid[i])

            # draw the grid
            for row in range(8):
                for column in range(8):
                    if (row + column) % 2 == 0:
                        color = white
                    else:
                        color = black
                    pygame.draw.rect(screen, color, [(margin + width) * column + margin, (margin + height) * row + margin, width, height])

            # set the white pieces on the grid
            for row in range(8):
                for column in range(8):
                    if grid[row][column] in white_pieces:
                        screen.blit(sprites[grid[row][column]], (column * 100, row * 100))

            # set the black pieces on the grid
            for row in range(8):
                for column in range(8):
                    if grid[row][column] in black_pieces:
                        screen.blit(sprites[grid[row][column]], (column * 100, row * 100))

    pygame.display.flip()
    return selected_piece, grid

# make the white pieces list
white_pieces = [
    "WhiteRook", "WhiteKnight", "WhiteBishop", "WhiteQueen", "WhiteKing", "WhiteBishop", "WhiteKnight", "WhiteRook",
    "WhitePawn", "WhitePawn", "WhitePawn", "WhitePawn", "WhitePawn", "WhitePawn", "WhitePawn", "WhitePawn"
]

# make the black pieces list
black_pieces = [
    "BlackPawn", "BlackPawn", "BlackPawn", "BlackPawn", "BlackPawn", "BlackPawn", "BlackPawn", "BlackPawn",
    "BlackRook", "BlackKnight", "BlackBishop", "BlackQueen", "BlackKing", "BlackBishop", "BlackKnight", "BlackRook"
]

black_pawn_moves = [
    [1, 0],
    [2, 0]
]

black_pawn_moves_1 = [
    [1, 0]
]

black_pawn_kill_moves = [
    [1, 1],
    [1, -1]
]

white_pawn_moves = [
    [-1, 0],
    [-2, 0]
]

white_pawn_moves_1 = [
    [-1, 0]
]

white_pawn_kill_moves = [
    [-1, 1],
    [-1, -1]
]

up_verticle_rook_moves = [
    [1, 0],
    [2, 0],
    [3, 0],
    [4, 0],
    [5, 0],
    [6, 0],
    [7, 0]
]

down_verticle_rook_moves = [
    [-1, 0],
    [-2, 0],
    [-3, 0],
    [-4, 0],
    [-5, 0],
    [-6, 0],
    [-7, 0]
]

left_horizontal_rook_moves = [
    [0, 1],
    [0, 2],
    [0, 3],
    [0, 4],
    [0, 5],
    [0, 6],
    [0, 7]
]

right_horizontal_rook_moves = [
    [0, -1],
    [0, -2],
    [0, -3],
    [0, -4],
    [0, -5],
    [0, -6],
    [0, -7]
]

knight_moves = [
    [1, 2],
    [2, 1],
    [-1, 2],
    [-2, 1],
    [1, -2],
    [2, -1],
    [-1, -2],
    [-2, -1]
]

up_left_bishop_moves = [
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4],
    [5, 5],
    [6, 6],
    [7, 7],
]

up_right_bishop_moves = [
    [-1, 1],
    [-2, 2],
    [-3, 3],
    [-4, 4],
    [-5, 5],
    [-6, 6],
    [-7, 7]
]

down_left_bishop_moves = [
    [1, -1],
    [2, -2],
    [3, -3],
    [4, -4],
    [5, -5],
    [6, -6],
    [7, -7]
]

down_right_bishop_moves = [
    [-1, -1],
    [-2, -2],
    [-3, -3],
    [-4, -4],
    [-5, -5],
    [-6, -6],
    [-7, -7]
]

up_right_queen_moves = [
    [-1, 1],
    [-2, 2],
    [-3, 3],
    [-4, 4],
    [-5, 5],
    [-6, 6],
    [-7, 7]
]

up_left_queen_moves = [
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4],
    [5, 5],
    [6, 6],
    [7, 7]
]

down_right_queen_moves = [
    [-1, -1],
    [-2, -2],
    [-3, -3],
    [-4, -4],
    [-5, -5],
    [-6, -6],
    [-7, -7]
]

down_left_queen_moves = [
    [1, -1],
    [2, -2],
    [3, -3],
    [4, -4],
    [5, -5],
    [6, -6],
    [7, -7]
]

up_verticle_queen_moves = [
    [1, 0],
    [2, 0],
    [3, 0],
    [4, 0],
    [5, 0],
    [6, 0],
    [7, 0]
]

down_verticle_queen_moves = [
    [-1, 0],
    [-2, 0],
    [-3, 0],
    [-4, 0],
    [-5, 0],
    [-6, 0],
    [-7, 0]
]

left_horizontal_queen_moves = [
    [0, 1],
    [0, 2],
    [0, 3],
    [0, 4],
    [0, 5],
    [0, 6],
    [0, 7]
]

right_horizontal_queen_moves = [
    [0, -1],
    [0, -2],
    [0, -3],
    [0, -4],
    [0, -5],
    [0, -6],
    [0, -7]
]

king_moves = [
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1],
    [-1, -1],
    [-1, 0],
    [-1, 1]
]

# set the black pieces on the grid
for i in range(8):
    grid[0][i] = black_pieces[i + 8]
    screen.blit(sprites[black_pieces[i + 8]], (i * 100, 0))
    grid[1][i] = black_pieces[i]
    screen.blit(sprites[black_pieces[i]], (i * 100, 100))
    
# set the white pieces on the grid
for i in range(8):
    grid[6][i] = white_pieces[i + 8]
    screen.blit(sprites[white_pieces[i + 8]], (i * 100, 600))
    grid[7][i] = white_pieces[i]
    screen.blit(sprites[white_pieces[i]], (i * 100, 700))
    
# print the grid
for i in range(8):
    print(grid[i])
        
# update the screen
pygame.display.flip()

# keep the screen open
while True:
            
    # check if the user pressed a piece
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            # print the piece that was pressed
            clicked = grid[row][column]
            print(clicked)
            selected_piece, grid = check_moves(clicked, row, column, selected_piece, grid)