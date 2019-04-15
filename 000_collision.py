import pygame
import sys
from random import random, randint

pygame.init()

high = 300
width = 500
screen = pygame.display.set_mode((width, high))
pygame.display.set_caption('I am the window')


def little_sqr(pos_x=0, pos_y=0):
    pygame.draw.rect(screen, (0, 255, 0), (pos_x, pos_y, 20, 20))


y = randint(0, 200)
x = randint(0, 200)
speed = 0.01

while True:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    """
    if int(y) == high:
        y -= (y * speed) + 5

    elif high > int(y) > 0:
        y += (y * speed) + 5

    elif int(x) == high:
        x -= x * speed

    elif int(x) == 0:
        x += x * speed

    #else:
    #    x += x * speed
    #    y += y * speed
    """
    x += speed
    y += speed

    print(200, int(y))

    little_sqr(pos_x=200, pos_y=y)

    pygame.display.update()
