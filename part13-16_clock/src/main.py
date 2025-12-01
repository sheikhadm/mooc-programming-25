# WRITE YOUR SOLUTION HERE:
# import pygame

# pygame.init()
# display = pygame.display.set_mode((640, 480))
# display.fill((0, 0, 0))

# pygame.draw.circle(display, (255, 0, 0), (300, 200), 10)
# pygame.draw.line(display, (0, 0, 255), (280, 350), (300, 200), 4)
# pygame.draw.line(display, (0, 0, 255), (350, 100), (300, 200), 1)
# pygame.draw.line(display, (0, 0, 255), (280, 350), (300, 200), 2)

# pygame.display.flip()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
import pygame
import math
import datetime

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

cx, cy = 320, 240  # center of the clock
radius = 200       # radius of circle


def hand_position(cx, cy, length, angle_degrees):
    # Convert degrees to radians
    angle = math.radians(angle_degrees - 90)  # -90 to make 0° point upward
    x = cx + math.cos(angle) * length
    y = cy + math.sin(angle) * length
    return (x, y)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    # Draw clock circle
    pygame.draw.circle(window, (250, 0, 0), (cx, cy), radius, 4)

    # Get current time
    now = datetime.datetime.now()
    hour = now.hour % 12
    minute = now.minute
    second = now.second

    # Convert to angles
    second_angle = second * 6                 # 60 seconds → 360 degrees
    minute_angle = minute * 6 + second * 0.1  # minute moves slightly with seconds
    hour_angle = hour * 30 + minute * 0.5     # hour moves slightly with minutes

    # Get end points
    hour_end = hand_position(cx, cy, 100, hour_angle)
    minute_end = hand_position(cx, cy, 150, minute_angle)
    second_end = hand_position(cx, cy, 180, second_angle)

    # Draw hands
    pygame.draw.line(window, (0, 0, 255), (cx, cy), hour_end, 4)
    pygame.draw.line(window, (0, 0, 255), (cx, cy), minute_end, 2)
    pygame.draw.line(window, (0, 0, 255), (cx, cy), second_end, 1)

    pygame.display.update()
    clock.tick(60)
