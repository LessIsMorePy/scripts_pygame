import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('I am the window')

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
