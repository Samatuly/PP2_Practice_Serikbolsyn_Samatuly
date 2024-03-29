from os import scandir
from select import select
import pygame, random, time

pygame.init()

# standardized elements
WHITE = (230, 230, 230)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 102)
LINE_COLOR = (50, 50, 50)
HEIGHT = 402
WIDTH = 402
BLOCK_SIZE = 20
SPEED = 5
LENGTH = 1
GAMEOVER = 0
LEVEL = 1
font_small = pygame.font.SysFont("comicsansms", 20)

# coordinates
class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
    
    # to draw square to a place of "#"
    def draw(self):
        for point in self.body:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (226,135,67), rect)

class Food:
    def __init__(self):
        self.location = Point(4, 10)

    # to draw food
    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (0, 255, 0), rect)


class Snake:
    def __init__(self):
        self.body = [Point(10, 11)]
        self.dx = 0
        self.dy = 0
        self.level = 1

    # to move snake through its previous parts of body
    def move(self):    
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.dx 
        self.body[0].y += self.dy 

        # borders to not go out the window
        if self.body[0].x * BLOCK_SIZE > WIDTH - 3:
            time.sleep(2)
            pygame.quit()
        if self.body[0].y * BLOCK_SIZE > HEIGHT - 3:
            time.sleep(2)
            pygame.quit()
        if self.body[0].x < 0:
            time.sleep(2)
            pygame.quit()
        if self.body[0].y < 0:
            time.sleep(2)
            pygame.quit()

    # to draw snake's head
    def draw(self):
        point = self.body[0]
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (255, 0, 0), rect)

        # to draw other parts of snake
        for point in self.body[1:]:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (0, 255, 0), rect)

    # to check if snake's head and food collide, snake will be increased in length 
    def check_collision(self, food):
        global LENGTH
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                LENGTH += 1
                if LENGTH % 4 == 0:
                    global LEVEL
                    LEVEL += 1
                    global SPEED
                    SPEED += 0.5
                food.location.x = random.randint(0, 19)
                food.location.y = random.randint(0, 19)
                self.body.append(Point(food.location.x, food.location.y))

    # to check if snake's head and its body collide, you wil lose
    def check_collision2(self):
        for i in range(len(self.body) - 1):
            if self.body[0].x == self.body[i].x and i != 0:
                if self.body[0].y == self.body[i].y and i != 0:
                    time.sleep(2)
                    pygame.quit()

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    snake = Snake()
    food = Food()

    while True:
        pygame.display.set_caption('Snake Game')
        # to exit from pygame window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # to create colgical movement. If snake is going up, it can't move down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and snake.dx != -1:
                    snake.dx = 1
                    snake.dy = 0
                if event.key == pygame.K_LEFT and snake.dx != 1:
                    snake.dx = -1
                    snake.dy = 0                      
                if event.key == pygame.K_UP and snake.dy != 1:
                    snake.dx = 0
                    snake.dy = -1
                if event.key == pygame.K_DOWN and snake.dy != -1:
                    snake.dx = 0
                    snake.dy = 1
        
        snake.move()

        snake.check_collision(food)

        SCREEN.fill(BLACK)

        snake.draw()
        food.draw()
        drawGrid()

        level_value = font_small.render("Level: " + str(LEVEL), True, RED)
        value = font_small.render("Length: " + str(LENGTH), True, RED)
        SCREEN.blit(level_value, (8, 20))
        SCREEN.blit(value, (8, 0))

        pygame.display.update()
        CLOCK.tick(5)

# to create grid
def drawGrid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, LINE_COLOR, rect, 1)


main()