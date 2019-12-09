import pygame, Player as p, Enemy as e
import random as r
pygame.init()

score = 0
screen_height = 600
screen_width =  600
screen = pygame.display.set_mode((screen_width, screen_height))
# title and screen
pygame.display.set_caption("XO")

hitSound = pygame.mixer.Sound("hit.wav")
backgroundSound = pygame.mixer.Sound("background.wav")

enemies = []

def ScoreRender():
    font = pygame.font.SysFont('Times New Roman', 30,True)
    text = font.render('Score: ' + str(score), 1, (0, 255, 255))
    screen.blit(text, (0, 0))

def EnemyRender(man):
    global score
    new_x = r.randint(screen_width / 2, screen_width)
    new_y = r.randint(0, screen_height)
    enemy = e.Enemy(new_x, new_y, 20, 20)
    enemies.append(enemy)

    for enemy in enemies:
        enemy.draw(screen)
    for enemy in enemies:
        s = True
        if (man.isCollide(enemy)):
            score+= 1
            enemies.pop(enemies.index(enemy))
        else:
            for bullet in man.bullets:
                if (bullet.isCollide(enemy)):
                    enemies.pop(enemies.index(enemy))
                    man.bullets.pop(man.bullets.index(bullet))
                    hitSound.play()
                    score += 1
                    break


def main():
    global score, enemies
    def renderWindow():
        screen.fill((0, 0, 0))
        man.draw(screen)
        EnemyRender(man)
        ScoreRender()
        backgroundSound.stop()
        pygame.display.update()

    man = p.Player(310, 410, 20, 20)
    running = True
    while (running):
        pygame.time.delay(200)
        keys = pygame.key.get_pressed()
        if (score <= 100):
 #           backgroundSound.play()
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if (keys[pygame.K_LEFT] and man.x > man.vel):
                man.x -= man.vel
            if (keys[pygame.K_RIGHT] and man.x < screen_width - man.width - man.vel):
                man.x += man.vel
            if (not man.isJump):
                if (keys[pygame.K_UP] and man.y > man.vel):
                    man.y -= man.vel
                if (keys[pygame.K_DOWN] and man.y < screen_height - man.height - man.vel):
                    man.y += man.vel
                if (keys[pygame.K_SPACE]):
                    if (score < 200):
                        man.fire()
                    else:
                        score = 0
                        enemies = []
                    #man.isJump = True
            else:
                if (man.jumpCount >= -10):
                    neg =  1
                    if (man.jumpCount < 0):
                        neg = -1
                    man.y -= (man.jumpCount ** 2) * 0.5 * neg
                    man.jumpCount -= 1
                else:
                    man.isJump = False
                    man.jumpCount = 10
            renderWindow()
        else:
            enemies = []
            man.bullets = []
            backgroundSound.play()
            screen.fill((0, 0, 255))
            pygame.display.update()
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False
            if (keys[pygame.K_SPACE]):
                score = 0
    pygame.quit()

if __name__ == "__main__":
    main()
