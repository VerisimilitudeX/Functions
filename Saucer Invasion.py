#### ---- LIBRARIES ---- ####
import tsk
import pygame
pygame.init()

#### ---------------------------- ####
#### ---- DRAW SHIP FUNCTION ---- ####
#### ---------------------------- ####
def draw_ship(w, center_x, center_y):

    # --- Colors --- #
    metal = (100, 100, 100)
    bright_metal = (220, 220, 220)
    light_color = (200, 255, 200)

    # --- Body layers --- #
    body = pygame.Rect(center_x - 100, center_y - 50, 200, 100)
    pygame.draw.ellipse(w, metal, body)
    highlight = pygame.Rect(center_x - 150, center_y - 20, 300, 50)
    pygame.draw.ellipse(w, bright_metal, highlight)
    ring = pygame.Rect(center_x - 150, center_y - 25, 300, 50)
    pygame.draw.ellipse(w, metal, ring)

    # --- Lights --- #
    start = center_x - 75
    width = 21
    height = 35
    light_y = center_y - int(height / 2) - 10
    for i in range(4):

        light = pygame.Rect(start + (width * 2 * i), light_y, width, height)

        pygame.draw.ellipse(w, light_color, light)

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

# --- Background --- #
w = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("AlienSpace.jpg", 0, 0)
background.draw()

#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:
    
    # --- Event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           drawing = False

        # --- Draw on mouse click --- #
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            draw_ship(w, x, y)

    # --- Finish --- #
    pygame.display.flip()
