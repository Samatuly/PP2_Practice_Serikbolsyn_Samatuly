import pygame, random, time

pygame.init()

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
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
font_small = pygame.font.SysFont("comicsansms", 20)
font_gameover = pygame.font.SysFont("comicsansms", 35)
game_over = font_gameover.render("Game Over", True, BLACK)
    
class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

class Food(pygame.sprite.Sprite):
    def __init__(self):
        self.location = Point(random.randint(1, 19), random.randint(1, 19))

    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, GREEN, rect)

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        self.body = [Point(10, 11)]
        self.dx = 0
        self.dy = 0

    def move(self):    
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y
        global GAMEOVER
        self.body[0].x += self.dx 
        self.body[0].y += self.dy 

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

    def draw(self):
        point = self.body[0]
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, RED, rect)


        for point in self.body[1:]:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, GREEN, rect)

    def check_collision(self, food):
        global LENGTH
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                LENGTH += 1
                if LENGTH % 3 == 0:
                    global SPEED
                    SPEED += 0.5
                food.location.x = random.randint(0, 19)
                food.location.y = random.randint(0, 19)
                self.body.append(Point(food.location.x, food.location.y))

    def check_collision2(self):
        for i in range(len(self.body) - 1):
            if self.body[0].x == self.body[i].x and i != 0:
                if self.body[0].y == self.body[i].y and i != 0:
                    time.sleep(2)
                    pygame.quit()

def main():
    pygame.init()
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)
    pygame.display.set_caption('Snake Game')

    snake = Snake()
    food = Food()

    INC_SPEED = pygame.USEREVENT + 1
    pygame.time.set_timer(INC_SPEED, 1000)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
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
        snake.check_collision2()

        SCREEN.fill(WHITE)
        pygame.draw.rect(SCREEN, RED, pygame.Rect(0, 0, 402, 402), 2)

        snake.draw()
        food.draw()

        value = font_small.render(str(LENGTH), True, RED)
        SCREEN.blit(value, (8, 0))

        pygame.display.update()
        CLOCK.tick(SPEED)
main()