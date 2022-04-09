import pygame
from pygame.locals import *

pygame.init()

isPressed = False
RED = (255, 0, 0)
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
Eraser = False

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_e]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                isPressed = True
            if event.type == pygame.MOUSEBUTTONUP:
                isPressed = False
            if event.type == pygame.MOUSEMOTION:         
                (x, y) = pygame.mouse.get_pos()
            if isPressed:
                pygame.draw.circle(screen, (0, 0, 0, 0), (x, y), 10)
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                isPressed = True
            if event.type == pygame.MOUSEBUTTONUP:
                isPressed = False
            if event.type == pygame.MOUSEMOTION:         
                (x, y) = pygame.mouse.get_pos()
            if isPressed:
                pygame.draw.circle(screen, (RED), (x, y), 10)
    pygame.display.flip()