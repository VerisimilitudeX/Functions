import random
import tsk
import pygame
pygame.init()

w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Pyramids.jpg", 0, 0)
sprite_names = ["AbeeFlyFront.png", "AdaLookingBack.png", "DolphinTrainer2.png", "FlyWorking.png", "GorillaBat.png", "IsaacFrogs.png", "KidPurpleShirt.png", "MascotBullCheer.png", "MascotLionVictory.png"]
sprite_spawn = 500
all_sprites = [background]

def sprite_name(sprite):
    print("The pyramids were filled with a " + sprite.image)

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    if sprite_spawn <= 0:
        sprite_spawn = 50
        index = random.randint(0, len(sprite_names) - 1)
        decoration = tsk.Sprite(sprite_names[index], random.randint(0, 1000), random.randint(0, 500))
        all_sprites.append(decoration)

        sprite_name(decoration)

    for sprite in all_sprites:
        sprite.draw()

    pygame.display.flip()
    c.tick(30)
    sprite_spawn -= c.get_time()
