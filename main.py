import pygame

pygame.display.set_mode((800, 800))
pygame.display.set_caption("Tomydas Chess")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False