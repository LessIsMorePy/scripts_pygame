import pygame
from pygame.locals import *     # For the pressed keys
import sys

# Init pygame
pygame.init()

# Screen settings
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('I am the window')

# Loop
while True:

    # Get events
    for event in pygame.event.get():

        # Get events when press some key
        if event.type == pygame.KEYDOWN:

            key = pygame.key.get_pressed()

            if key[K_w]:
                screen.fill(pygame.Color('blue'))

            elif key[K_a]:
                screen.fill(pygame.Color('red'))

            elif key[K_d]:
                screen.fill(pygame.Color('green'))

        # Get events when release some key
        if event.type == pygame.KEYUP:

            key = pygame.key.get_pressed()

            if key[K_w]:
                screen.fill(pygame.Color('black'))

            elif key[K_a]:
                screen.fill(pygame.Color('black'))

            elif key[K_d]:
                screen.fill(pygame.Color('black'))

        # Close window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update screen
    pygame.display.update()
