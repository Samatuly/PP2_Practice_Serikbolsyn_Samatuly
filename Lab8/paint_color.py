import pygame
from pygame.locals import *

pygame.init()

isPressed = False
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 20, 147)
ORANGE = (255, 100, 10)
VIOLET = (148, 0, 211)

screen = pygame.display.set_mode((500, 500))

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        pressed_keys = pygame.key.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN:
                isPressed = True
        if event.type == pygame.MOUSEBUTTONUP:
                isPressed = False
        if event.type == pygame.MOUSEMOTION:         
                (x, y) = pygame.mouse.get_pos()
        if isPressed:
                pygame.draw.circle(screen, (RED), (x, y), 10)
        if pressed_keys[K_g]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                isPressed = True
            if event.type == pygame.MOUSEBUTTONUP:
                isPressed = False
            if event.type == pygame.MOUSEMOTION:         
                (x, y) = pygame.mouse.get_pos()
            if isPressed:
                pygame.draw.circle(screen, (GREEN), (x, y), 10)
        elif pressed_keys[K_b]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                isPressed = True
            if event.type == pygame.MOUSEBUTTONUP:
                isPressed = False
            if event.type == pygame.MOUSEMOTION:         
                (x, y) = pygame.mouse.get_pos()
            if isPressed:
                pygame.draw.circle(screen, (BLUE), (x, y), 10)
        elif pressed_keys[K_w]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                isPressed = True
            if event.type == pygame.MOUSEBUTTONUP:
                isPressed = False
            if event.type == pygame.MOUSEMOTION:         
                (x, y) = pygame.mouse.get_pos()
            if isPressed:
                pygame.draw.circle(screen, (WHITE), (x, y), 10)
        elif pressed_keys[K_y]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                isPressed = True
            if event.type == pygame.MOUSEBUTTONUP:
                isPressed = False
            if event.type == pygame.MOUSEMOTION:         
                (x, y) = pygame.mouse.get_pos()
            if isPressed:
                pygame.draw.circle(screen, (YELLOW), (x, y), 10)
        elif pressed_keys[K_p]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                isPressed = True
            if event.type == pygame.MOUSEBUTTONUP:
                isPressed = False
            if event.type == pygame.MOUSEMOTION:         
                (x, y) = pygame.mouse.get_pos()
            if isPressed:
                pygame.draw.circle(screen, (PURPLE), (x, y), 10)
        elif pressed_keys[K_o]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                isPressed = True
            if event.type == pygame.MOUSEBUTTONUP:
                isPressed = False
            if event.type == pygame.MOUSEMOTION:         
                (x, y) = pygame.mouse.get_pos()
            if isPressed:
                pygame.draw.circle(screen, (ORANGE), (x, y), 10)
        elif pressed_keys[K_v]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                isPressed = True
            if event.type == pygame.MOUSEBUTTONUP:
                isPressed = False
            if event.type == pygame.MOUSEMOTION:         
                (x, y) = pygame.mouse.get_pos()
            if isPressed:
                pygame.draw.circle(screen, (VIOLET), (x, y), 10)
        elif pressed_keys[K_e]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                isPressed = True
            if event.type == pygame.MOUSEBUTTONUP:
                isPressed = False
            if event.type == pygame.MOUSEMOTION:         
                (x, y) = pygame.mouse.get_pos()
            if isPressed:
                pygame.draw.circle(screen, (0, 0, 0, 0), (x, y), 10)
    pygame.display.flip()