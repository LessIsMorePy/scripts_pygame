import pygame

pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('I am the window')

# Used to mange how fast the screen updates
clock = pygame.time.Clock()

# Initial loop state
done = False

# Color
green = (0, 255, 0)

while not done:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

    # Draw on the screen several lines from (0, 10) to (100, 100)
    for y_offset in range(0, 100, 15):
        pygame.draw.line(screen, green, [0, y_offset], [100, 100 + y_offset], 3)

    # Update the screen with what we have draw
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit
pygame.quit()
