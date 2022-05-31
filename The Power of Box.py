#### ---- LIBRARIES ---- ####
import random
import tsk
import pygame
pygame.init()

#### ------------------------------- ####
#### ---- ATTRACT CATS FUNCTION ---- ####
#### ------------------------------- ####

def attract_cats(z, x, y):
    if cat_filenames < 0:
        cat_filenames = 0    

    cat_filenames = ["BoredCat.png", "BrownAndWhiteCat.png", "Cat.png", "FluffyCat.png"]
    for cat in cat_filenames:

        catx = random.randint(x - 450, x + 450)
        caty = random.randint(y - 200, y + 200)

        if catx < (x - 100) or catx > (x + 100):
            catx += 200

        # --- Make cat --- #
        index = random.randint(0, len(cat_filenames) - 1)
        sprite = tsk.Sprite(cat_filenames[index])
        sprite.center_x = catx
        sprite.center_y = caty

        # --- Flip cats on the right --- #
        if sprite.center_x > catx:
            sprite.flip_x = True


        # --- Draw cat --- #
        sprite.draw()
        pygame.display.flip()

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
w = pygame.display.set_mode([1018, 573])

# --- Background --- #
tsk.Sprite("CatRoom.jpg", 0, 0).draw()

# --- Box --- #
box = tsk.Sprite("CatBox.png", 1018//2, 573//2)
box.draw()
pygame.display.flip()

#### ---- MAIN LOOP ---- ####
while True:

    # --- Event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    # --- Get user input --- #
    if input("More cats?! (enter or type stop) ") == "stop":
        break

    attract_cats(random.randint(1, 7), box.center_x, box.center_y)

    # --- Finish --- #
    pygame.display.flip()
