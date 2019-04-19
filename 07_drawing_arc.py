import pygame
import math

pygame.init()

screen = pygame.display.set_mode((400, 350))
pygame.display.set_caption('I am the window')

# Used to mange how fast the screen updates
clock = pygame.time.Clock()

# Initial loop state
done = False

# Color
color = (200, 0, 200)
color1 = (200, 200, 0)
color2 = (10, 40, 200)
color3 = (100, 250, 200)

while not done:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

    # Draw arc
    pygame.draw.arc(screen, color, [50, 50, 250, 200], math.pi/2, math.pi, 2)
    pygame.draw.arc(screen, color1, [50, 50, 250, 200], 0, math.pi/2, 2)
    pygame.draw.arc(screen, color2, [50, 50, 250, 200], 3*math.pi / 2, 2*math.pi, 2)
    pygame.draw.arc(screen, color3, [50, 50, 250, 200], math.pi, 3*math.pi/2, 2)

    # Update the screen with what we have draw
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit
pygame.quit()
