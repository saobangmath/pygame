import pygame, Bullet as b
class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 20
        self.isJump = False
        self.jumpCount = 10
        self.right = False
        self.left = False
        self.walkCount = 0
        self.bullets = []

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

        for bullet in self.bullets:
           bullet.draw(screen)

    def fire(self):
        bullet = b.Bullet(self.x, self.y)
        self.bullets.append(bullet)
