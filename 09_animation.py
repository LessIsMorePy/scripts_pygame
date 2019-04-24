import pygame
from random import randint

pygame.init()

high = 300
weight = 300

screen = pygame.display.set_mode((weight, high))
pygame.display.set_caption('I am the window')

# Used to mange how fast the screen updates
clock = pygame.time.Clock()

# Initial loop state
done = False

# Initial position
pos_x = randint(0, weight)
pos_y = randint(0, weight)
pos_x1 = randint(0, weight)
pos_y1 = randint(0, weight)

# Speed
speed_x = randint(0, 10)
speed_y = randint(0, 10)
speed_x1 = randint(0, 10)
speed_y1 = randint(0, 10)

# Square area
area = 20

# Settings text
font = pygame.font.SysFont('Calibri', 15, True, False)

while not done:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

    # Text
    for var, num, scale in [(pos_x, 0, 0), (pos_y, 1, 15), (pos_x1, 2, 30), (pos_y1, 3, 45)]:

        text = "pos_x%s: %s" % (num, var)
        pos = font.render(text, True, (255, 255, 255))
        screen.blit(pos, [0, scale])

    # Direction
    if pos_x > (high - area) or pos_x < 0:
        speed_x = - speed_x * 1

    if pos_y > (high - area) or pos_y < 0:
        speed_y = - speed_y * 1

    if pos_x1 > (high - area) or pos_x1 < 0:
        speed_x1 = - speed_x1 * 1

    if pos_y1 > (high - area) or pos_y1 < 0:
        speed_y1 = - speed_y1 * 1

    color1 = (randint(0, 255), randint(0, 255), randint(0, 255))
    color2 = (randint(0, 255), randint(0, 255), randint(0, 255))

    pygame.draw.rect(screen, color1, [pos_x, pos_y, area, area])
    pygame.draw.rect(screen, color2, [pos_x1, pos_y1, area, area])

    pos_x += speed_x
    pos_y += speed_y
    pos_x1 += speed_x1
    pos_y1 += speed_y1

    # Update the screen with what we have draw
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit
pygame.quit()
