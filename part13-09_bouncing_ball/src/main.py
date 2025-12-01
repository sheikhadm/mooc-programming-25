# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("ball.png")

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
    if y+robot.get_height() < 480 : 
        y += velocity

    if x_velocity > 0 and x+robot.get_width() >= 640 :
        x = 639 - robot.get_width()
        x_velocity = -x_velocity
    if x_velocity < 0 and x <= 0:
        x_velocity = -x_velocity
    if velocity > 0 and y+robot.get_height() >= 480 :
        y = 479 - robot.get_height()
        velocity = -velocity
    if velocity < 0 and y <= 0:
        velocity = -velocity
        
    

    # if velocity > 0 and y+robot.get_height() >= 480:
    #     velocity = -velocity
    # if velocity < 0 and y <= 0:
    #     velocity = -velocity
    

    clock.tick(60)