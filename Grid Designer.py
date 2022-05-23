#### ---- LIBRARIES ---- ####
import pygame
pygame.init()

#### ------------------- ####
#### ---- DRAW GRID ---- ####
#### ------------------- ####
def draw_grid(num_squares, square_size):
    # Validate input
    if num_squares >= 1 and num_squares <= 10 and square_size == 100:
        pass
    
    else:
        print("Lbozo")
        num_squares = 8
        square_size = 100

    w = pygame.display.set_mode([num_squares * 100, num_squares * 100])
    w.fill((255, 255, 255))

    for i in range(num_squares):
        for j in range(num_squares):
            if (i % 2) == 0:
                if (j % 2) == 0:
                    square = pygame.Rect(i * square_size, j * square_size, square_size, square_size)
                    pygame.draw.rect(w, (0, 0, 0), square)
            else:
                if (j % 2) == 1:
                    square = pygame.Rect(i * square_size, j * square_size, square_size, square_size)
                    pygame.draw.rect(w, (0, 0, 0), square)

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
squares = int(input("How big is your board (1 - 10)? "))
draw_grid(squares, 100)

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    pygame.display.flip()
