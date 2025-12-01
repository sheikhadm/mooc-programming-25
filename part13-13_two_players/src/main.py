# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
x = 0
y = 480-robot.get_height()
x_s = 50
y_s =50

to_right = False
to_left = False
to_up = False
to_down = False

to_secondright = False
to_secondleft = False
to_secondup = False
to_seconddown = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True
            if event.key == pygame.K_a:
                to_secondleft = True
            if event.key == pygame.K_d:
                to_secondright = True
            if event.key == pygame.K_w:
                to_secondup = True
            if event.key == pygame.K_s:
                to_seconddown = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False
            if event.key == pygame.K_a:
                to_secondleft = False
            if event.key == pygame.K_d:
                to_secondright = False
            if event.key == pygame.K_w:
                to_secondup = False
            if event.key == pygame.K_s:
                to_seconddown = False


        if event.type == pygame.QUIT:
            exit()

    if to_right and x +robot.get_width() <= 640:
        x += 2
    if to_left and x  > 0:
        x -= 2
    if to_down and y + robot.get_height() <= 480:
        y += 2
    if to_up and y  > 0:
        y -= 2
    if to_secondright and x_s +robot.get_width() <= 640:
        x_s += 2
    if to_secondleft and x_s  > 0:
        x_s -= 2
    if to_seconddown and y_s + robot.get_height() <= 480:
        y_s += 2
    if to_secondup and y_s  > 0:
        y_s -= 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot, (x_s, y_s))
    pygame.display.flip()

    clock.tick(60)