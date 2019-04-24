import pygame

pygame.init()

high = 300
weight = 300

screen = pygame.display.set_mode((weight, high))
pygame.display.set_caption('I am the window')

# Used to mange how fast the screen updates
clock = pygame.time.Clock()

# Colors
black = [0, 0, 0]
white = [255, 255, 255]

# Initial loop state
done = False
while not done:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

    # Update the screen with what we have draw
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit
pygame.quit()
