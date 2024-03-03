import engine
import pygame as pg
import utils

pg.init()

class Window:
    def __init__(self):
        self.screen = pg.display.set_mode((1200, 800))
        pg.display.set_caption("Plazma Chess")
        self.engine = engine.Engine()
        self.pieceFont = pg.font.SysFont("segoeuisymbol", 100)
        self.selectedSquare = None
        self.validMoves = ()

    def drawBoard(self):
        isWhite = False
        for y in range(8):
            isWhite = not isWhite
            for x in range(8):
                if isWhite: pg.draw.rect(self.screen, (150, 150, 0), (y*100, x*100, 100, 100))
                else: pg.draw.rect(self.screen, (50, 50, 50), (y*100, x*100, 100, 100))
                isWhite = not isWhite

        for move in self.validMoves: pg.draw.rect(self.screen, (255, 100, 100), (move[0]*100, move[1]*100, 100, 100))
        if self.selectedSquare != None: pg.draw.rect(self.screen, (255, 0, 0), (self.selectedSquare[0]*100, self.selectedSquare[1]*100, 100, 100))

    def drawPieces(self):
        for y in range(8):
            for x in range(8):
                piece = self.engine.board.board[y][x]
                if piece < 7:
                    if self.selectedSquare == (x, y):
                        pos = pg.mouse.get_pos()
                        self.screen.blit(self.pieceFont.render(utils.PIECE_UNICODES[self.engine.board.board[y][x]], True, (255, 255, 255)), (min(pos[0]-50, 750), pos[1]-70))
                    else:
                        self.screen.blit(self.pieceFont.render(utils.PIECE_UNICODES[self.engine.board.board[y][x]], True, (255, 255, 255)), (x*100, y*100-20))
                else:
                    if self.selectedSquare == (x, y):
                        pos = pg.mouse.get_pos()
                        self.screen.blit(self.pieceFont.render(utils.PIECE_UNICODES[self.engine.board.board[y][x]], True, (0, 0, 0)), (min(pos[0]-50, 750), pos[1]-70))
                    else:
                        self.screen.blit(self.pieceFont.render(utils.PIECE_UNICODES[self.engine.board.board[y][x]], True, (0, 0, 0)), (x*100, y*100-20))

    def run(self):
        clock = pg.time.Clock()
        while 1:
            self.drawBoard()
            self.drawPieces()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    if pos[0] < 800 and pos[1] < 800:
                        self.selectedSquare = (int(round((pos[0]-50)/100, 0)), int(round((pos[1]-50)/100, 0)))
                        piece = self.engine.board.board[self.selectedSquare[1]][self.selectedSquare[0]]
                        if piece == 0: self.selectedSquare = None
                        elif piece < 7 and self.engine.turn == 1: self.selectedSquare = None
                        elif piece > 6 and self.engine.turn == 0: self.selectedSquare = None
                        else: self.validMoves = self.engine.generateMoves(self.selectedSquare)

                if event.type == pg.MOUSEBUTTONUP and self.selectedSquare != None:
                    pos = pg.mouse.get_pos()
                    if pos[0] < 800 and pos[1] < 800:
                        try: self.engine.move(self.selectedSquare, (int(round((pos[0]-50)/100, 0)), int(round((pos[1]-50)/100, 0))))
                        except: self.engine.turn = not self.engine.turn
                    self.validMoves = ()
                    self.selectedSquare = None
                    self.engine.turn = not self.engine.turn

            pg.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    window = Window()
    window.run()
