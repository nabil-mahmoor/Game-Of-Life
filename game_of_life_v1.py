import pygame as pg
from pygame.locals import *
import random
import copy
import sys


pg.init()

DIMENSIONS = 10

WIDTH = 700
HEIGHT = 600
WINDOW = pg.display.set_mode((WIDTH, HEIGHT))

fpsClock = pg.time.Clock()
FPS = 60



def create_pattern():
    board = [[random.choice(['#', '-', '-', '-', '-', '-', '-']) for _ in range(WIDTH // DIMENSIONS)] for _ in range(HEIGHT // DIMENSIONS)]
    return board



def print_board(currentBoard):
    for i, row in enumerate(currentBoard):
        for j, value in enumerate(row):
            if value == '#':
                pg.draw.rect(WINDOW, 'black', (j * DIMENSIONS, i * DIMENSIONS, DIMENSIONS, DIMENSIONS))
                



def evolve(currentBoard, nextBoard):
    for i, row in enumerate(currentBoard):
        for j, value in enumerate(row):
            neighbors = find_neighbors(currentBoard, i, j)

            if value == '#' and (neighbors == 2 or neighbors == 3):
                nextBoard[i][j] = '#'
            elif value == '-' and neighbors == 3:
                nextBoard[i][j] = '#'
            else:
                nextBoard[i][j] = '-'

    return nextBoard



def find_neighbors(currentBoard, y, x):
    # initiate vatiables
    # NOTE: coordinates wrap around due to %
    top = (y - 1) % len(currentBoard)
    bottom = (y + 1) % len(currentBoard)
    left = (x - 1) % len(currentBoard[0])
    right = (x + 1) % len(currentBoard[0])

    neighbors = 0
    if currentBoard[top][left] == '#':   # topleft
        neighbors += 1
    if currentBoard[top][x] == '#':   # top
        neighbors += 1
    if currentBoard[top][right] == '#':   # topright
        neighbors += 1
    if currentBoard[y][right] == '#':   # right
        neighbors += 1
    if currentBoard[bottom][right] == '#':   # bottomright
        neighbors += 1
    if currentBoard[bottom][x] == '#':   # bottom
        neighbors += 1
    if currentBoard[bottom][left] == '#':   # bottomleft
        neighbors += 1
    if currentBoard[y][left] == '#':   # left
        neighbors += 1

    return neighbors



def draw_grid():
    # horizontal
    for i in range(HEIGHT // DIMENSIONS):
        pg.draw.line(WINDOW, 'grey', (0, i * DIMENSIONS), (WIDTH, i * DIMENSIONS))
    # vertical
    for i in range(WIDTH // DIMENSIONS):
        pg.draw.line(WINDOW, 'grey', (i * DIMENSIONS, 0), (i * DIMENSIONS, HEIGHT))



pattern = create_pattern()


COOLDOWN = 100
update_time = pg.time.get_ticks()
while True:
        for event in pg.event.get():
            if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pg.quit()
                sys.exit()

        if (pg.time.get_ticks() - update_time) > COOLDOWN:
            update_time = pg.time.get_ticks()
            nextPattern = copy.deepcopy(pattern)
            pattern = evolve(nextPattern, pattern)

        WINDOW.fill('white')
        draw_grid()

        print_board(pattern)
        
        pg.display.update()
        fpsClock.tick(FPS)