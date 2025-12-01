# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()

window.fill((0,0,0))

for x in range(1000):
    x_random = random.randint(0,640- width)
    y_random = random.randint(0,480- height)
    window.blit(robot, (x_random, y_random))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()