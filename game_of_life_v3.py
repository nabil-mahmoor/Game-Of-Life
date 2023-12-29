import pygame as pg
from pygame.locals import *
import random
import copy
import sys


pg.init()

COLORS = {
    '0': (3, 4, 50),
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
    # board[y][x] --> [cell, prev_neighbor, next_neighbor]
    board = [[[random.choice(['#', '-', '-', '-', '-', '-', '-']), '0', '0'] for _ in range(WIDTH // DIMENSIONS)] for _ in range(HEIGHT // DIMENSIONS)]
    return board



def print_board(board, alpha):
    for i, row in enumerate(board):
        for j, data in enumerate(row):
            current_color = lerp_color(COLORS[data[1]], COLORS[data[2]], alpha)
            pg.draw.rect(WINDOW, current_color, (j * DIMENSIONS, i * DIMENSIONS, DIMENSIONS, DIMENSIONS), border_radius=2)



def evolve(currentBoard, nextBoard):
    for i, row in enumerate(currentBoard):
        for j, data in enumerate(row):
            prev_color = data[2]
            neighbors = find_neighbors(currentBoard, i, j)

            if data[0] == '#' and (neighbors == 2 or neighbors == 3):
                nextBoard[i][j] = ['#', prev_color, str(neighbors)]
            elif data[0] == '-' and neighbors == 3:
                nextBoard[i][j] = ['#', prev_color, str(neighbors)]
            else:
                nextBoard[i][j] = ['-', prev_color, str(neighbors)]

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



# Interpolate between prev_color and next_color
def lerp_color(prev_color, next_color, alpha):
    # print(prev_color)
    r = int(prev_color[0] + (next_color[0] - prev_color[0]) * alpha)
    g = int(prev_color[1] + (next_color[1] - prev_color[1]) * alpha)
    b = int(prev_color[2] + (next_color[2] - prev_color[2]) * alpha)

    return r, g, b



newPattern = create_pattern()


TIMESTEP = 30
frame_count = 0
while True:
        for event in pg.event.get():
            if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pg.quit()
                sys.exit()

        alpha = min(frame_count / TIMESTEP, 1)

        frame_count += 1

        if alpha >= 1:
            frame_count = alpha = 0
            initialPattern = copy.deepcopy(newPattern)
            newPattern = evolve(initialPattern, newPattern)

        WINDOW.fill('black')
        print_board(newPattern, alpha)
        draw_grid()
        
        pg.display.update()
        fpsClock.tick(FPS)