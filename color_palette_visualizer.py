import pygame as pg
from pygame.locals import *

pg.init()

COLORS = {
    '0': (0, 0, 0),
    '1': (72, 202, 228),
    '2': (0, 180, 216),
    '3': (0, 150, 199),
    '4': (0, 119, 182),
    '5': (63, 55, 201),
    '6': (72, 12, 168),
    '7': (58, 12, 163),
    '8': (3, 4, 94)
}

COLORS = {
    '0': (0, 0, 0),
    '1': (255, 233, 169),
    '2': (255, 197, 24),
    '3': (255, 133, 40),
    '4': (181, 45, 200),
    '5': (104, 23, 197),
    '6': (60, 21, 150),
    '7': (45, 9, 131),
    '8': (33, 11, 86)
}

PALETTE_COUNT = 9
WIDTH = 900
HEIGHT = 200
PALETTE_WIDTH = WIDTH // PALETTE_COUNT

WINDOW = pg.display.set_mode((WIDTH, HEIGHT))
fps = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()

    for x, col in COLORS.items():
        pg.draw.rect(WINDOW, col, (int(x) * PALETTE_WIDTH, 0, PALETTE_WIDTH, HEIGHT), 0, 10)
    
    pg.display.update()
    fps.tick(60)