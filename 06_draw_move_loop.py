import pygame
import math

pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('I am the window')

# Used to mange how fast the screen updates
clock = pygame.time.Clock()

# Initial loop state
done = False

# Color
color = (200, 0, 200)

while not done:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

    for i in range(200):

        radians_x = i / 20
        radians_y = i / 6

        x = int(75 * math.sin(radians_x)) + 150
        y = int(75 * math.cos(radians_y)) + 150

        pygame.draw.line(screen, color, [x, y], [x + 5, y], 3)

    # Update the screen with what we have draw
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit
pygame.quit()
