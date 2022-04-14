import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()
X = False
RED   = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
TRANSPARENT = (0, 0, 0, 0)

# infinite background music until game over
pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)

# fonts to score to "game over"
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# to create screen, fill it and give name to the screen
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Street Racer: Endless Road")
 
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(65, SCREEN_WIDTH - 65), 0)  
    
    # if enemy goes off a screen, the enemy will be loaded randomly again
    def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(65, SCREEN_WIDTH - 65), 0)
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 540)
        
    def move(self):
        # movement of player
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            if self.rect.center[1] > 50:
                self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            if self.rect.center[1] < 555:
                self.rect.move_ip(0,5)
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                if self.rect.center[0] > 65:
                    self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                if self.rect.center[0] < 335:
                    self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Coin.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(65, SCREEN_WIDTH - 65), 0)

    # if coin goes off a screen, the coin will be loaded randomly again
    def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(65, SCREEN_WIDTH - 65), 0)
             
class Background():
    def __init__(self):
        self.street = pygame.image.load('AnimatedStreet.png')
        self.rectStreet = self.street.get_rect()
 
        self.bgY1 = 0
        self.bgX1 = 0
 
        self.bgY2 = self.rectStreet.height
        self.bgX2 = 0
 
        self.movingDownSpeed = 5
         
    # movement of background image(road)
    def update(self):
            self.bgY1 += self.movingDownSpeed
            self.bgY2 += self.movingDownSpeed
            if self.bgY1 >= self.rectStreet.height:
                self.bgY1 = -self.rectStreet.height
            if self.bgY2 >= self.rectStreet.height:
                self.bgY2 = -self.rectStreet.height
            
    def render(self):
        DISPLAYSURF.blit(self.street, (self.bgX1, self.bgY1))
        DISPLAYSURF.blit(self.street, (self.bgX2, self.bgY2))

# Sprites                    

 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.1    
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    P1 = Player()
    E1 = Enemy()
    C1 = Coin()
    back_ground = Background()
    enemies = pygame.sprite.Group()
    enemies.add(E1)
    money = pygame.sprite.Group()
    money.add(C1)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(P1)
    all_sprites.add(E1)
    all_sprites.add(C1)

    back_ground.update()
    back_ground.render()
    
    # code of score
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (15,10))
 
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # if player and money collides, money will be deleted
    if pygame.sprite.spritecollideany(P1, money):
        SCORE += 1
        for entity in money:
            entity.kill()


    # if player and enemy collides, you will lose and phrase "game over" will be showed
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.pause()
        pygame.mixer.Sound('crash.wav').play()
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)