# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Ten Robots in a Circle")

robot = pygame.image.load("robot.png")
clock = pygame.time.Clock()

angle = 0

# Number of robots
num_robots = 10
# Radius of circular path
radius = 120
# Center of circle
center_x, center_y = 320, 240

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))

    # Draw ten robots around a circle
    for i in range(num_robots):
        # Even spacing around circle
        current_angle = angle + (2 * math.pi / num_robots) * i

        x = center_x + math.cos(current_angle) * radius - robot.get_width() / 2
        y = center_y + math.sin(current_angle) * radius - robot.get_height() / 2

        window.blit(robot, (x, y))

    pygame.display.flip()

    angle += 0.01
    clock.tick(60)

pygame.quit()
