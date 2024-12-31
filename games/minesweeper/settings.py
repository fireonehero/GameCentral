# 5 is the lowest without overlap, 11 is the highest without resizing cells, 16 is highest without flooding
GRID_SIZE = 9
CELL_SIZE = 2
#This random number is PERFECT. Don't change
RANDOM_CONST = 52
MINE_COUNT = round((GRID_SIZE ** 2) / 6)

WIDTH = GRID_SIZE * RANDOM_CONST
HEIGHT = WIDTH + int(WIDTH / 4)

#Calculate  the size of the window, 
def set_grid_size(new_size):
    global GRID_SIZE
    global CELL_SIZE
    global MINE_COUNT
    global WIDTH
    global HEIGHT
    global RANDOM_CONST
    GRID_SIZE = new_size
    if GRID_SIZE > 10:
        CELL_SIZE = 1
        RANDOM_CONST = 35
    elif GRID_SIZE <= 10:
        CELL_SIZE = 2
        RANDOM_CONST = 52

    MINE_COUNT = round((GRID_SIZE ** 2) / 6)
    WIDTH = GRID_SIZE * RANDOM_CONST
    HEIGHT = WIDTH + int(WIDTH / 4)
