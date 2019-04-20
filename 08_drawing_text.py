import pygame
from random import randint

pygame.init()

screen = pygame.display.set_mode((250, 50))
pygame.display.set_caption('I am the window')

# Used to mange how fast the screen updates
clock = pygame.time.Clock()

# Initial loop state
done = False

# Settings text
font = pygame.font.SysFont('Calibri', 40, True, False)

i = 0

while not done:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

    i += 1

    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    score = font.render("Score: %s" % str(i), True, color)
    screen.blit(score, [0, 0])

    if i == 150:
        i = 0

    # Update the screen with what we have draw
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit
pygame.quit()
