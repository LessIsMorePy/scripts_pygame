import pygame

pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('I am the window')

# Used to mange how fast the screen updates
clock = pygame.time.Clock()

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
