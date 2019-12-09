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

    def isCollide(self, enemy):
        dx_center = abs(enemy.x - self.x)
        dy_center = abs(enemy.y - self.y)
        total_x = (enemy.width + self.width) / 2
        total_y = (enemy.height + self.height) / 2
        if (dx_center < total_x and dy_center < total_y):
            return True
        return False