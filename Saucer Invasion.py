"""
LESSON: 6.1 - Functions
EXERCISE: Saucer Invasion
"""

#### ---- LIBRARIES ---- ####

# Import the tsk library
import tsk

# Import pygame
import pygame

# Initialize pygame
pygame.init()

#### ---------------------------- ####
#### ---- DRAW SHIP FUNCTION ---- ####
#### ---------------------------- ####
# DEFINE the draw_ship function, with PARAMETERS window,
# center_x, and center_y
def draw_ship(w, center_x, center_y):

    # --- Colors --- #

    # Create a color called metal with the value
    # (100, 100, 100)
    metal = (100, 100, 100)

    # Create a color called bright_metal with the value
    # (220, 220, 220)
    bright_metal = (220, 220, 220)

    # Create a color called light_color with the value
    # (200, 255, 200)
    # ---> TEST AFTER THIS LINE <--- #
    light_color = (200, 255, 200)

    # --- Body layers --- #

    # Create a Rect called body with left center_x - 100,
    # top center_y - 50, width 200, and height 100
    body = pygame.Rect(center_x - 100, center_y - 50, 200, 100)

    # Draw the body Rect as an ellipse in window with
    # color metal
    # ---> TEST AFTER THIS LINE <--- #
    pygame.draw.ellipse(w, metal, body)

    # Create a Rect called highlight with left
    # center_x - 150, top center_y - 20, width 300, and
    # height 50
    highlight = pygame.Rect(center_x - 150, center_y - 20, 300, 50)

    # Draw the highlight Rect as an ellipse in window
    # with color bright_metal
    pygame.draw.ellipse(w, bright_metal, highlight)

    # Create a Rect called ring with left center_x - 150,
    # top center_y - 25, width 300, and height 50
    ring = pygame.Rect(center_x - 150, center_y - 25, 300, 50)

    # Draw the ring Rect as an ellipse in window with
    # color metal
    # ---> TEST AFTER THIS LINE <--- #
    pygame.draw.ellipse(w, metal, ring)

    # --- Lights --- #

    # Create a variable called start with the value
    # center_x - 75
    start = center_x - 75

    # Create a variable width with value 21
    width = 21

    # Create a variable height with value 35
    height = 35

    # Create a variable light_y with value center_y -
    # the integer result of height / 2, then - 10
    light_y = center_y - int(height / 2) - 10

    # For i in a range of 4
    for i in range(4):

        # Create a Rect called light with left start +
        # (width * 2 * i), a top light_y, width, and
        # height
        light = pygame.Rect(start + (width * 2 * i), light_y, width, height)

        # Draw the light Rect as an ellipse in window
        # with light_color
        # ---> TEST AFTER THIS LINE <--- #
        pygame.draw.ellipse(w, light_color, light)

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

# --- Background --- #

# Create a window w with width 1018 and height 573
w = pygame.display.set_mode([1018, 573])

# Create a background sprite from the image
# "AlienSpace.jpg" at position 0, 0
background = tsk.Sprite("AlienSpace.jpg", 0, 0)

# Draw the background sprite
# ---> TEST AFTER THIS LINE <--- #
background.draw()

#### ---- MAIN LOOP ---- ####

# Create a variable called drawing with value True
drawing = True

# While drawing
while drawing:
    
    # --- Event loop --- #

    # Create an event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           drawing = False

        # --- Draw on mouse click --- #

        # Check for the MOUSEBUTTONDOWN event
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Get mouse position and store it in x, y
            x, y = pygame.mouse.get_pos()

            # CALL the draw_ship function with
            # ARGUMENTS w, x, and y
            draw_ship(w, x, y)

    # --- Finish --- #

    # Flip the display
    pygame.display.flip()

# Turn in your Coding Exercise.