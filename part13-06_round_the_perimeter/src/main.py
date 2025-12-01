# # WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 1
x_velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    if x+robot.get_width() < 640  : 
        x += x_velocity
    if y+robot.get_height() < 480 and x+robot.get_width() >= 640 : 
        y += velocity
    if y+robot.get_height() < 480 and x <= 0 : 
        y += velocity
    if x_velocity > 0 and x+robot.get_width() >= 640 and y + robot.get_height() >= 480:
        x = 639 - robot.get_width()
        x_velocity = -x_velocity
    if x_velocity < 0 and x <= 0:
        velocity = -velocity
        x_velocity = 0
        y= 479 -robot.get_height()
    if x <= 0 and y <= 0:
        velocity = -velocity
        x_velocity = 1

    # if velocity > 0 and y+robot.get_height() >= 480:
    #     velocity = -velocity
    # if velocity < 0 and y <= 0:
    #     velocity = -velocity
    

    clock.tick(60)