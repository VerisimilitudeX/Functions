"""
LESSON: 6.1 - Functions
EXERCISE: The Power of Box
"""

#### ---- LIBRARIES ---- ####
#
# Import and set up random, tsk, and pygame libraries
import random
import tsk
import pygame
pygame.init()
#
#### ------------------------------- ####
#### ---- ATTRACT CATS FUNCTION ---- ####
#### ------------------------------- ####
#
# Define the function with parameters for the number
# of cats and the x and y positions to draw around####################
###################////////////////////////////////////////
def attract_cats(z, x, y):
#
    # --- Validate input --- #

    # If the number of cats is negative, set it to 0
    # ---> TEST AFTER THIS LINE <--- #
    if cat_filenames < 0:
        cat_filenames = 0    
#
    # --- Cat creation loop --- #
#
    # Create a list with the cat filenames:
    # "BoredCat.png", "BrownAndWhiteCat.png", "Cat.png",
    #  and "FluffyCat.png"
    cat_filenames = ["BoredCat.png", "BrownAndWhiteCat.png", "Cat.png", "FluffyCat.png"]
##
    # Loop through the total number of cats
    for cat in cat_filenames:
#
        # --- Get random location --- #
#
        # Pick a random location for the cat that's
        # within 450 pixels left or right of the x
        # position and within 200 pixels above or below
        # the y position
        catx = random.randint(x - 450, x + 450)
        caty = random.randint(y - 200, y + 200)
#
        # If the cat's x position is within 100 pixels
        # left or right of the main x position, move
        # the cat's position right by 200
        if catx < (x - 100) or catx > (x + 100):
            catx += 200

        # --- Make cat --- #

        # Choose a random filename from the list of cat
        # images, and create a sprite with its center
        # at the chosen random x and y positions
        index = random.randint(0, len(cat_filenames) - 1)
        sprite = tsk.Sprite(cat_filenames[index])
        sprite.center_x = catx
        sprite.center_y = caty

        # --- Flip cats on the right --- #

        # If the cat is to the right of the draw point,
        # flip the sprite image horizontally
        if sprite.center_x > catx:
            sprite.flip_x = True


        # --- Draw cat --- #

        # Draw the cat
        # ---> TEST AFTER THIS LINE <--- #
        sprite.draw()
        pygame.display.flip()

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

# Create a 1018 x 573 window
w = pygame.display.set_mode([1018, 573])
# --- Background --- #

# Create a draw a background sprite using "CatRoom.jpg"
tsk.Sprite("CatRoom.jpg", 0, 0).draw()

# --- Box --- #

# Create a sprite with "CatBox.png" in roughly the
# middle of the window, draw it, and flip the display
box = tsk.Sprite("CatBox.png", 1018//2, 573//2)
box.draw()
pygame.display.flip()

#### ---- MAIN LOOP ---- ####

# Create a main loop
while True:

    # --- Event loop --- #

    # Create an event loop
    # ---> TEST AFTER THIS LINE <--- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    # --- Get user input --- #

    # Get input from the user and quit the main loop
    # if the user entered "stop"
    # ---> TEST AFTER THIS LINE <--- #
    if input("More cats?! (enter or type stop) ") == "stop":
        break

    # Otherwise, call the function to randomly draw
    # 1 - 7 cats around the box's center
    attract_cats(random.randint(1, 7), box.center_x, box.center_y)


    # --- Finish --- #

    # Flip the display
    pygame.display.flip()

# Turn in your Coding Exercise.