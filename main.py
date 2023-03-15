import pygame
import sys

pygame.init()

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
    "BlackPawn": pygame.image.load("Sprites/Black Pawn.png")
}

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

# set the white pieces on the grid
for i in range(8):
    grid[0][i] = white_pieces[i]
    screen.blit(sprites[white_pieces[i]], (i * 100, 0))
    grid[1][i] = white_pieces[i + 8]
    screen.blit(sprites[white_pieces[i + 8]], (i * 100, 100))
    
# set the black pieces on the grid
for i in range(8):
    grid[6][i] = black_pieces[i]
    screen.blit(sprites[black_pieces[i]], (i * 100, 600))
    grid[7][i] = black_pieces[i + 8]
    screen.blit(sprites[black_pieces[i + 8]], (i * 100, 700))
    
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
            print(grid[row][column])
            
# Path: main.py