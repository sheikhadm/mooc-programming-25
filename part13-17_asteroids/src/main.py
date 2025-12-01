# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame
import random
 
score = 0
pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
game_font = pygame.font.SysFont("Arial", 24)
text = game_font.render(f"points: 0", True, (255, 0, 0))

robot_img = pygame.image.load("rock.png")
robot = pygame.image.load('robot.png')

x = 0
y = 480-robot.get_height()
to_right = False
to_left = False

GROUND_LEVEL = 480 - robot_img.get_height()

class Robot:
    def __init__(self):
        self.x = random.randint(0, 640 - robot_img.get_width())
        self.y = -robot_img.get_height()
        self.is_off = False
        self.fall_speed = 2

        # Phase 1: falling straight down
        self.falling = True

        # Phase 2: walking left or right
        self.walk_speed = random.choice([-2, 2])  # choose left or right

    def update(self,x,y):
        if self.falling:
            # FALLING
            self.y += self.fall_speed
            if self.y == y and (self.x > x and self.x <x+ robot.get_width()):
                self.is_off = True
                return True

    def draw(self):
        window.blit(robot_img, (self.x, self.y))

    def is_off_screen(self):
        if self.y > 480:
            return True
    
    def x(self):
        return self.x
    def y(self):
        return self.y

robots = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
           
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
           
        
    if to_right and x +robot.get_width() <= 640:
        x += 3
    if to_left and x  > 0:
        x -= 3

    # Spawn new robots
    if random.random() < 0.005:
        robots.append(Robot())

    # Update all robots
    for r in robots:
        if r.update(x,y):
            score += 1
            text = game_font.render(f"points: {score}", True, (255, 0, 0))
        if r.is_off_screen():
            exit()
            

    # Remove robots that walk off-screen
    robots = [r for r in robots if not r.is_off]


    window.fill((0, 0, 0))

    # Draw robots
    for r in robots:
        r.draw()
    window.blit(robot, (x, y))
    window.blit(text, (500, 0))
    pygame.display.update()
    clock.tick(60)
