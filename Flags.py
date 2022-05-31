#### ---- LIBRARIES --- ####
import tsk
import random
import pygame
pygame.init()

#### --------------------------- ####
#### ---- DRAW BEE FUNCTION ---- ####
#### --------------------------- ####
def draw_bee(direction):
    x = random.randint(0, 950)
    y = random.randint(0, 500)
    bee = tsk.Sprite("Bee.png", x, y)
    if direction == "left":
        bee.flip_x = True

    bee.draw()

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
w = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("OutdoorBushes.jpg", 0, 0)
background.draw()

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                draw_bee("left")
            elif event.key == pygame.K_RIGHT:
                draw_bee("right")
                
    pygame.display.flip()
