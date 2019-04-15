import pygame
import sys

pygame.init()

high = 300
width = 500

screen = pygame.display.set_mode((width, high))
pygame.display.set_caption('I am the window')

spriteSheet = pygame.image.load("descarga.png").convert_alpha()


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    image = pygame.transform.scale(spriteSheet.subsurface((0, 0, 100, 100)), (50, 50))
    rect = image.get_rect()
    # Donde se situa la imagen.
    rect.center = (screen.get_width() / 2, screen.get_height() / 2)

    grupo_sprites = pygame.sprite.GroupSingle()

    grupo_sprites.draw(screen)

    pygame.display.update()
