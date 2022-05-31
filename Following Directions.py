#### ---- LIBRARIES ---- ####
import tsk, random, pygame
pygame.init()


#### ----------------------------- ####
#### ---- DRAW ARROW FUNCTION ---- ####
#### ----------------------------- ####

# Create a function that takes parameters for the
# window, direction of the arrow, and arrow color
def drw_arw(w, direction, color):

    # --- Arrow body --- #

    # If the direction was left or right, create a
    # wide, horizontal rectangle for the arrow's base,
    # otherwise, make it a tall, vertical rectangle
    # ---> TEST AFTER THIS LINE <--- #





    # --- Arrow point --- #

    # Pick three points to make a triangle for the
    # arrow's point, based on the direction it will be
    # pointing


















    # --- Arrow color --- #

    # Create a tuple for the arrow's color based on the
    # arrow color parameter (red or green)






    # --- Draw arrow --- #

    # Draw the rectangle and the triangle using the
    # chosen color to make the arrow
    # ---> TEST AFTER THIS LINE <--- #




#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

#### ---- SETUP ---- ####
# --- Program setup --- #
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

# --- Sprites --- #
background = tsk.Sprite("ScienceLab.jpg", 0, 0)
robot = tsk.Sprite("RobotDance.png", 100, 150)

# --- Arrow setup --- #
arrow = "left"
arrow_color = "red"
arrow_timer = 0
arrow_limit = 1000
directions = ["left", "right", "up", "down"]

# --- Score variables --- #
score = 0
mistakes = 0


#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:


    #### ---- EVENT LOOP ---- ####
    for event in pygame.event.get():

        # --- Quit --- #
        if event.type == pygame.QUIT:
            drawing = False

        # --- Key Press --- #

        # If a keyboard key was pressed


            # If the key pressed corresponds to the
            # current direction in the arrow variable,
            # (i.e. pygame.K_RIGHT and "right", etc.)
            # then set the arrow color to "green" and
            # increment the score




            # Otherwise, increase mistakes by 1
            # ---> TEST AFTER THIS LINE <--- #




    #### ---- ARROW ---- ####

    # --- Switch to new arrow if necessary --- #

    # If the arrow_timer is more than the arrow_limit



        # --- Lose a try if you missed the arrow --- #

        # If arrow_color is still "red", increase
        # mistakes by 1




        # --- New direction --- #

        # Set arrow to a random direction from the
        # directions list




        # --- Re-set color --- #

        # Set arrow_color to "red"



        # --- Re-set and reduce time limit -- #

        # Return the arrow_timer to 0, and reduce the
        # arrow_limit if it's still more than half a
        # second





    #### ---- DRAW SCENE ---- ####

    background.draw()
    robot.draw()

    # Call the draw_arrow function with w, arrow, and
    # the arrow_color



    #### ---- FINISH ---- ####

    # Increase the arrow_timer by the frame time


    pygame.display.flip()
    c.tick(30)

    # End the loop if the user has made too many
    # mistakes
    # ---> TEST AFTER THIS LINE <--- #



#### ---- FINAL OUTPUT ---- ####

# Output the final score
# ---> TEST AFTER THIS LINE <--- #






# Turn in your Coding Exercise.
