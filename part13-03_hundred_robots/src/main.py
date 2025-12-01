# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()

window.fill((0,0,0))
def ten_in_row(x_point,y_point):
    
    for x in range(10):
        window.blit(robot, (x_point, y_point))
        x_point = x_point + 40 
y_point = 90
x_point = 50
for x in range(10):
    
    ten_in_row(x_point,y_point)
    y_point += 20
    x_point += 10

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
