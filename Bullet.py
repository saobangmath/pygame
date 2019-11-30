import pygame
class Bullet(object):
    def __init__(self, x, y):
        self.vel = 20
        self.x = x
        self.y = y
        self.height = 10
        self.width = 10

    def draw(self, screen):
        self.x += self.vel
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.width, self.height))

    def isCollide(self, enemy):
        dx_center = abs(enemy.x - self.x)
        dy_center = abs(enemy.y - self.y)
        total_x = (enemy.width + self.width) / 2
        total_y = (enemy.height + self.height) / 2
        if (dx_center < total_x and dy_center < total_y):
            return True
        return False


