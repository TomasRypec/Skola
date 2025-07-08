import pygame
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Donut properties
donut_color = (222, 184, 135)
hole_color = (40, 40, 40)
x, y = 100, HEIGHT // 2
speed_x = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move donut
    x += speed_x
    if x > WIDTH + 50:
        x = -50

    # Draw
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, donut_color, (x, y), 50)
    pygame.draw.circle(screen, hole_color, (x, y), 20)
    pygame.display.flip()
    clock.tick(60)