"""
LESSON: 6.1 - Functions
WARMUP 3
"""

# Libraries
import random
import tsk
import pygame
pygame.init()


#### ------------------------------------ ####
#### ---- PRINT SPRITE NAME FUNCTION ---- ####
#### ------------------------------------ ####
def sprite_name(sprite):
    print("The living room was decorated with a " + sprite.image)

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####

# Program variables
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

# Sprites
background = tsk.Sprite("LivingRoom.jpg", 0, 0)
sprite_names = ["BalloonPink.png", "BalloonRed.png", "BushVase1.png", "BushVase2.png", "BushVase3.png", "ShortVase.png"]
sprite_spawn = 1500
all_sprites = [background]

#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # Move sprites
    if sprite_spawn <= 0:
        sprite_spawn = 1500
        index = random.randint(0, len(sprite_names) - 1)
        decoration = tsk.Sprite(sprite_names[index], random.randint(0, 1000), random.randint(0, 500))
        all_sprites.append(decoration)

        # Call function here
        sprite_name(decoration)

    # Draw frame
    for sprite in all_sprites:
        sprite.draw()

    # Finish
    pygame.display.flip()
    c.tick(30)
    sprite_spawn -= c.get_time()

