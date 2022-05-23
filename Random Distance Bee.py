import random
import tsk
import pygame
pygame.init()

w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

timer = 3000
bees = []
background = tsk.Sprite("OutdoorBushes.jpg", 0, 0)
for i in range(10):
    bee = tsk.Sprite("Bee.png", 0, 50 + (i * 50))
    bees.append(bee)

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    for bee in bees:
        bee.x += random.randint(1, 20) * 0.025 * c.get_time()

    background.draw()
    for bee in bees:
        bee.draw()

    timer -= c.get_time()
    pygame.display.flip()
    c.tick(30)

    if timer <= 0:
        drawing = False

max_x = 0
for bee in bees:
    if bee.x > max_x:
        max_x = bee.x

print("The farthest bee was at " + str(max_x))
