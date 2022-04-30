from os import scandir
from select import select
import pygame, random, time, psycopg2

username = str(input("Your name: "))
if(len(username) >= 1) and (username[0] != " "):
    pygame.init()
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)

# standardized elements
LOSE = False
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
SCORE = 0
COUNTER = 7
LEVEL = 1
font_small = pygame.font.SysFont("comicsansms", 20)
font_big = pygame.font.SysFont("comicsansms", 40)
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
        global COUNTER
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        self.food = pygame.draw.rect(SCREEN, (0, 255, 0), rect)
        if COUNTER == 0:
            point.x = random.randint(0, 19)
            point.y = random.randint(0, 19)
            pygame.draw.rect(SCREEN, (0, 255, 0), rect)
            COUNTER = 7

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
            global LOSE
            LOSE = True
        elif self.body[0].y * BLOCK_SIZE > HEIGHT - 3:
            LOSE = True
        elif self.body[0].x < 0:
            LOSE = True
        elif self.body[0].y < 0:
            LOSE = True

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
        global LENGTH, SCORE, COUNTER, LEVEL
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                LENGTH += 1
                COUNTER = 7
                SCORE += random.randrange(1, 5)
                if LENGTH % 4 == 0:
                    global SPEED
                    LEVEL += 1
                    SPEED += 0.5
                food.location.x = random.randint(0, 19)
                food.location.y = random.randint(0, 19)
                self.body.append(Point(food.location.x, food.location.y))

    # to check if snake's head and its body collide, you will lose
    def check_collision2(self):
        global LOSE
        for i in range(len(self.body) - 1):
            if self.body[0].x == self.body[i].x and i != 0:
                if self.body[0].y == self.body[i].y and i != 0:
                    LOSE = True

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
            global COUNTER
            if event.type == pygame.USEREVENT:
                COUNTER -= 1
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
        snake.check_collision2()

        SCREEN.fill(BLACK)

        snake.draw()
        food.draw()
        drawGrid()
        if(LOSE):
            game_over()
            pygame.quit()

        level_value = font_small.render("Level: " + str(LEVEL), True, RED)
        value = font_small.render("Score: " + str(SCORE), True, RED)
        username_value = font_small.render("Name:     " + username, True, WHITE)
        score_value = font_small.render("Score:     " + str(SCORE), True, WHITE)
        gameover_value = font_big.render("GAME OVER", True, WHITE)

        SCREEN.blit(level_value, (8, 20))
        SCREEN.blit(value, (8, 0))

        def game_over():
            time.sleep(1)
            SCREEN.fill(RED)
            SCREEN.blit(gameover_value, (75, 150))
            SCREEN.blit(username_value, (100, 210))
            SCREEN.blit(score_value, (100, 230))
            save_result(username, SCORE)
            print("Your result saved successfully")

        pygame.display.update()
        CLOCK.tick(5)

# to create grid
def drawGrid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, LINE_COLOR, rect, 1)

def save_result(username, SCORE):
    conn = psycopg2.connect("dbname=postgres user=postgres password=Serik2004")
    cur = conn.cursor()
    cur.execute("Insert into public.snake(nickname, user_score) values('%s', '%s')" % (username, SCORE))
    conn.commit()
    conn.close()

main()