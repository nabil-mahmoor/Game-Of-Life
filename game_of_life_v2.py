import pygame as pg
from pygame.locals import *
import random
import copy
import sys


pg.init()

COLORS = {
    '0': (0, 0, 0),
    '1': (76, 201, 240),
    '2': (67, 97, 238),
    '3': (114, 9, 183),
    '4': (114, 9, 183),
    '5': (114, 9, 183),
    '6': (58, 12, 163),
    '7': (58, 12, 163),
    '8': (58, 12, 163)
}

DIMENSIONS = 10

WIDTH = 900
HEIGHT = 600
WINDOW = pg.display.set_mode((WIDTH, HEIGHT))

fpsClock = pg.time.Clock()
FPS = 60



def create_pattern():
    board = [[(random.choice(['#', '-', '-', '-', '-', '-', '-']), '0') for _ in range(WIDTH // DIMENSIONS)] for _ in range(HEIGHT // DIMENSIONS)]
    return board



def print_board(currentBoard):
    for i, row in enumerate(currentBoard):
        for j, data in enumerate(row):
            pg.draw.rect(WINDOW, COLORS[data[1]], (j * DIMENSIONS, i * DIMENSIONS, DIMENSIONS, DIMENSIONS), border_radius=2)



def evolve(currentBoard, nextBoard):
    for i, row in enumerate(currentBoard):
        for j, data in enumerate(row):
            neighbors = find_neighbors(currentBoard, i, j)

            if data[0] == '#' and (neighbors == 2 or neighbors == 3):
                nextBoard[i][j] = ('#', str(neighbors))
            elif data[0] == '-' and neighbors == 3:
                nextBoard[i][j] = ('#', str(neighbors))
            else:
                nextBoard[i][j] = ('-', str(neighbors))

    return nextBoard



def find_neighbors(currentBoard, y, x):
    # initiate vatiables
    # NOTE: coordinates wrap around due to %
    top = (y - 1) % len(currentBoard)
    bottom = (y + 1) % len(currentBoard)
    left = (x - 1) % len(currentBoard[0])
    right = (x + 1) % len(currentBoard[0])

    neighbors = 0
    if currentBoard[top][left][0] == '#':   # topleft
        neighbors += 1
    if currentBoard[top][x][0] == '#':   # top
        neighbors += 1
    if currentBoard[top][right][0] == '#':   # topright
        neighbors += 1
    if currentBoard[y][right][0] == '#':   # right
        neighbors += 1
    if currentBoard[bottom][right][0] == '#':   # bottomright
        neighbors += 1
    if currentBoard[bottom][x][0] == '#':   # bottom
        neighbors += 1
    if currentBoard[bottom][left][0] == '#':   # bottomleft
        neighbors += 1
    if currentBoard[y][left][0] == '#':   # left
        neighbors += 1

    return neighbors



def draw_grid():
    # horizontal
    for i in range(HEIGHT // DIMENSIONS):
        pg.draw.line(WINDOW, 'black', (0, i * DIMENSIONS), (WIDTH, i * DIMENSIONS))
    # vertical
    for i in range(WIDTH // DIMENSIONS):
        pg.draw.line(WINDOW, 'black', (i * DIMENSIONS, 0), (i * DIMENSIONS, HEIGHT))



pattern = create_pattern()


TIMESTEP = 100
update_time = pg.time.get_ticks()
while True:
        for event in pg.event.get():
            if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pg.quit()
                sys.exit()

        if (pg.time.get_ticks() - update_time) > TIMESTEP:
            update_time = pg.time.get_ticks()
            nextPattern = copy.deepcopy(pattern)
            pattern = evolve(nextPattern, pattern)

        WINDOW.fill('black')
        print_board(pattern)
        draw_grid()
        
        pg.display.update()
        fpsClock.tick(FPS)