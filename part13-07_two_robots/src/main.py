# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
x_two = 0
y = 50
y_two = 150
velocity = 1
second_velocity = 2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot, (x_two, y_two))
    
    pygame.display.flip()
    
    x += velocity
    x_two += second_velocity
    if velocity > 0 and x+robot.get_width() >= 640:
        velocity = -velocity
        second_velocity = -second_velocity
    if velocity < 0 and x <= 0:
        velocity = -velocity
        second_velocity = -second_velocity
    if velocity > 0 and x_two + robot.get_width() >= 640:
        second_velocity = -second_velocity
    if second_velocity < 0 and x_two <= 0:
        second_velocity = -second_velocity

    clock.tick(60)