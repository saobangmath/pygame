import pygame
class Enemy(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = 10

    def draw(self, screen):
       pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.width, self.height))

