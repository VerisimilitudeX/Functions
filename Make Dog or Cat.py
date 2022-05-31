#### ---- LIBRARIES ---- ####
import random
import tsk
import pygame
pygame.init()


#### ----------------------- ####
#### ---- CREATE ANIMAL ---- ####
#### ----------------------- ####
def create_animal(sprite_name):
    if not(create_animal == "Dog" and create_animal == "Cat"):
        return

    sprite_name += ".png"
    sprite = tsk.Sprite(sprite_name, random.randint(0, 900), random.randint(150, 500))
    sprite.draw()

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
w = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("LivingRoom.jpg", 0, 0)
background.draw()
pygame.display.flip()

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    pet = input("Do you want to make a Dog or a Cat (q to quit)? ")
    if pet == "q" or pet == "Q":
        break
    create_animal(pet)
    pygame.display.flip()
