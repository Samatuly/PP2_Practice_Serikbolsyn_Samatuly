import pygame
import random
from pygame import mixer
pygame.init()
mixer.init()
screen = pygame.display.set_mode((600, 600))
done = False
pos = 0
songs = ['Opr-Gesaffelstein.mp3', 'Eminem-Venom.mp3', 'No-Roots-Alice-Merton.mp3']
pygame.mixer.music.load(songs[pos])
pygame.mixer.music.play()
pygame.mixer.music.queue(songs[random.randrange(0, 4)])
while not done:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done == True
            pygame.quit()
            exit()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            if pos >= 1:
                pos -= 1
            else:
                pos = 2
        elif pressed[pygame.K_SPACE]:
            pygame.mixer.music.pause()
        elif pressed[pygame.K_LALT]:
            pygame.mixer.music.unpause()
        pygame.mixer.music.load(songs[pos])
        pygame.mixer.music.play()
        if pressed[pygame.K_RIGHT]:
            if pos < 2:
                pos += 1
            else:
                pos = 0
        screen.fill((255,200,255))
        pygame.display.flip()