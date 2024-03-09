# Plazma Chess Engine

## In development!

### This is a basic chess engine based off of the [python-chess](https://github.com/niklasf/python-chess) library

#### The engine comes with a client which supports multiplayer, singleplayer and bot chess matches!

Try running ```python example.py``` to test the engine or just play with friends

## Documentation
### Setting up the board
```python
import engine # Import the plazma-chess module

chessEngine = engine.Engine() # Create instance of the Engine class
```

This will initialize the engine class which contains all of the information of the board.
All pieces will be set to normal chess starting positions.

### Acessing the board
```python
import engine # Import the plazma-chess module

chessEngine = engine.Engine() # Create instance of the Engine class
print(chessEngine.board.board) # Access the board class stored in the engine class and get the board list

# Example output of starting positions
"""[[10, 8, 9, 11, 12, 9, 8, 10],
    [7, 7, 7, 7, 7, 7, 7, 7],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [4, 2, 3, 5, 6, 3, 2, 4]]"""
```
To Access the board class, and the board list within that you need to use the engine class.
This is because when the engine class is initialized it also initializes the board.

### Generating moves
```python
import engine # Import the plazma-chess module

chessEngine = engine.Engine() # Create instance of the Engine class

legalMoves = chessEngine.GenerateMoves((4, 6)) # Get the legal moves for the kings pawn
```
To get the legal moves for a piece you just need to specify the coordinates of the piece and call the GenerateMoves function in the engine class, passing in those coordinates.

### Finding pieces
```python
import engine # Import the plazma-chess module

chessEngine = engine.Engine() # Create instance of the Engine class

pos = any_pieces_position

print(chessEngine.board.pieceAt(pos)) # Call the 'pieceAt' function in the board
# Prints:
#   bool -> Found a piece
#   int -> Piece value (0 if no piece)
```