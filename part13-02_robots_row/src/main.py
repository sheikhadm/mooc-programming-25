# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()
width_robot = 550-width
window.fill((0,0,0))
for x in range(10):
    window.blit(robot, (width_robot, 100))
    width_robot = width_robot - width

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
