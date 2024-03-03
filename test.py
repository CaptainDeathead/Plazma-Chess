import pygame as pg

pg.init()

screen = pg.display.set_mode((200, 200))

font = pg.font.SysFont("segoeuisymbol", 100)

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    pg.draw.rect(screen, (0, 0, 0), (0, 0, 100, 100))
    pg.draw.rect(screen, (255, 255, 255), (100, 0, 100, 100))
    pg.draw.rect(screen, (255, 255, 255), (0, 100, 100, 100))
    pg.draw.rect(screen, (0, 0, 0), (100, 100, 100, 100))
    pg.draw.line(screen, (255, 0, 0), (0, 100), (200, 100), 5)
    pg.draw.line(screen, (255, 0, 0), (100, 0), (100, 200), 5)

    screen.blit(font.render("♙", True, (255, 255, 255)), (0, 0))
    screen.blit(font.render("♙", True, (0, 0, 0)), (0, 100))
    screen.blit(font.render("♟︎", True, (0, 0, 0)), (100, 0))
    screen.blit(font.render("♟︎", True, (255, 255, 255)), (100, 100))

    pg.display.flip()