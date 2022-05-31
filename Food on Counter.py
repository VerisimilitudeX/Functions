import random
import tsk
import pygame
pygame.init()

#### ---------------------------- ####
#### ---- DRAW FOOD FUNCTION ---- ####
#### ---------------------------- ####
def draw_food(number):
    if number > 5 or number < 1:
        return
    files = ["BurgerPatty.png", "CheeseSlice.png", "HamSlice.png", "LettuceLeaf.png", "TomatoSlice.png"]
    image  = files[number - 1]
    food = tsk.Sprite(image, random.randint(0, 750), random.randint(400, 500))
    food.draw()

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

w = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("Restaurant.jpg", 0, 0)
background.draw()
pygame.display.flip()

#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    value = int(input("Enter a number, 1 - 5 or 0 to quit "))

    draw_food(value)

    pygame.display.flip()
    if value == 0:
        drawing = False
