# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

robot_img = pygame.image.load("robot.png")

GROUND_LEVEL = 480 - robot_img.get_height()

class Robot:
    def __init__(self):
        self.x = random.randint(0, 640 - robot_img.get_width())
        self.y = -robot_img.get_height()
        self.fall_speed = random.randint(2, 6)

        # Phase 1: falling straight down
        self.falling = True

        # Phase 2: walking left or right
        self.walk_speed = random.choice([-2, 2])  # choose left or right

    def update(self):
        if self.falling:
            # FALLING
            self.y += self.fall_speed

            # Did we reach the ground?
            if self.y >= GROUND_LEVEL:
                self.y = GROUND_LEVEL
                self.falling = False   # switch to walking

        else:
            # WALK LEFT OR RIGHT
            self.x += self.walk_speed

    def draw(self):
        window.blit(robot_img, (self.x, self.y))

    def is_off_screen(self):
        return (self.x < -robot_img.get_width()) or (self.x > 640)

robots = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Spawn new robots
    if random.random() < 0.05:
        robots.append(Robot())

    # Update all robots
    for r in robots:
        r.update()

    # Remove robots that walk off-screen
    robots = [r for r in robots if not r.is_off_screen()]

    window.fill((0, 0, 0))

    # Draw robots
    for r in robots:
        r.draw()

    pygame.display.update()
    clock.tick(60)
