from turtle import position
import pygame

def main():
    pygame.init()

    # Window size
    screen = pygame.display.set_mode((640, 480))

    baseLayer = pygame.Surface((640, 480))

    clock = pygame.time.Clock()
    
    # Coordinates of previous and current point
    prevX = -1
    prevY = -1
    currentX = -1
    currentY = -1
        
    screen.fill((0, 0, 0))

    isMouseDown = False

    while True:
        
        pressed = pygame.key.get_pressed()

        # code that helps to exit from pygame window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            # when mouse is pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]    
                    prevX =  event.pos[0]
                    prevY =  event.pos[1]

            # when we stopped to press a mouse
            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baseLayer.blit(screen, (0, 0))

            # when arrow of mouse is moving
            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
        
        # formula to create shape that we need
        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
             screen.blit(baseLayer, (0, 0))
             r = [[prevX, prevY], [prevX, currentY], [currentX, prevY]]
             pygame.draw.polygon(screen, (255,255, 255), r)
        
        pygame.display.flip()
        clock.tick(60)

main()