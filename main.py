import pygame
import sys

pygame.init()

# make a grid of 8x8
grid = [[0 for x in range(8)] for y in range(8)]

# make the white pieces list
white_pieces = [
    "Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook",
    "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn"
]

# make the black pieces list
black_pieces = [
    "Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook",
    "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn"
]

# set the white pieces on the grid
for i in range(8):
    grid[0][i] = white_pieces[i]
    grid[1][i] = white_pieces[i + 8]
    
# set the black pieces on the grid
for i in range(8):
    grid[7][i] = black_pieces[i]
    grid[6][i] = black_pieces[i + 8]
    
# print the grid
for i in range(8):
    print(grid[i])

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

# draw the grid
for row in range(8):
    for column in range(8):
        if (row + column) % 2 == 0:
            color = white
        else:
            color = black
        pygame.draw.rect(screen, color, [(margin + width) * column + margin, (margin + height) * row + margin, width, height])
        
# update the screen
pygame.display.flip()

# keep the screen open
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
# Path: main.py