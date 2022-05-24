"""
LESSON: 6.1 - Functions
TECHNIQUE 3: Draw at Offset
DEMO
"""

#### ---- LIBRARIES ---- ####
import tsk
import pygame
pygame.init()


#### ---------------------- ####
#### ---- DRAW SPRITES ---- ####
#### ---------------------- ####
def draw_sprites(x, y):
    panda = tsk.Sprite("PandaPilot.png", 0, 0)
    puffin = tsk.Sprite("PuffinWalk.png", 0, 0)

    panda.center_x = x
    panda.center_y = y
    puffin.center_x = -20
    puffin.center_y = -280

    panda.draw()
    puffin.draw()


#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
w = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("SkyMountains.jpg", 0, 0)
x = 0
y = 0

#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        # Mouse input
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

    # Draw
    background.draw()
    draw_sprites(x, y)
    pygame.display.flip()