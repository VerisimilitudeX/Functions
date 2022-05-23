"""
LESSON: 6.1 - Functions
WARMUP 1
"""

import random
import tsk
import pygame
pygame.init()



# Main program
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

timer = 3000
bees = []
background = tsk.Sprite("OutdoorBushes.jpg", 0, 0)
for i in range(10):
    bee = tsk.Sprite("Bee.png", 0, 50 + (i * 50))
    bees.append(bee)

# Main loop
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # Move bees here
    for bee in bees:
        bee.x += random.randint(1, 20) * 0.025 * c.get_time()

    # Draw
    background.draw()
    for bee in bees:
        bee.draw()

    # Finish
    timer -= c.get_time()
    pygame.display.flip()
    c.tick(30)

    if timer <= 0:
        drawing = False

# Find winning bee here
max_x = 0
for bee in bees:
    if bee.x > max_x:
        max_x = bee.x

print("The farthest bee was at " + str(max_x))