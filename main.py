import pygame as pg


# Window size
win_width = 800
win_height = 800

# Initialize the pg library
pg.init()

# Creating the window with caption
win = pg.display.set_mode((win_width, win_height))
pg.display.set_caption("Tic Tac Toe")

# Game variables
start_game = False

run = True

while run:
    win.fill((200, 220, 240))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.update()
pg.quit()