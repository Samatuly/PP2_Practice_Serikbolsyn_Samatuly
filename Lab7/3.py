import pygame
pygame.init()
a = int(input("Write size of a screen: "))
screen = pygame.display.set_mode((a, a))
done = False
step = 20
x = a / 2
y = a / 2

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done == True
            pygame.quit()
            exit()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            if(y - step >= 25):
                y -= step
            else:
                while y - step <= 25:
                    step -= 1
                    if(y - step == 25):
                        y -= step
        step = 20
        if pressed[pygame.K_DOWN]:
            if(y + step <= a - 25):
                y += step
            else:
                while y + step >= a - 25:
                    step -= 1
                    if(y + step == a - 25):
                        y += step
        step = 20
        if pressed[pygame.K_LEFT]:
            if(x - step >= 25):
                x -= step
            else:
                while x - step <= 25:
                    step -= 1
                    if(x - step == 25):
                        x -= step
        step = 20
        if pressed[pygame.K_RIGHT]:
            if(x + step <= a - 25):
                x += step
            else:
                while x + step >= a - 25:
                    step -= 1
                    if(x + step == a - 25):
                        x += step
        step = 20
        screen.fill((255,200,255))
        pygame.draw.circle(screen, (255,0,0), [x, y], 25, 0)
        pygame.display.flip()