import pygame
import random

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sprite Color Change Event")

WHITE =(255, 255, 255)
BLACK = (0, 0, 0)

class ColorSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def change_color(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(self.color)

sprites = pygame.sprite.Group()
for i in range(5): 
    sprite = ColorSprite(i * 60 + 50, height // 2, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    sprites.add(sprite)
COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(COLOR_CHANGE_EVENT, 2000) 
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == COLOR_CHANGE_EVENT:
            for sprite in sprites:
                sprite.change_color()  
    sprites.draw(screen) 
    pygame.display.flip()  

pygame.quit()
