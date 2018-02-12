import pygame

clock = pygame.time.Clock()
radius = 200
iteration = 0
loop = True
screen = pygame.display.set_mode((400, 400))

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    if iteration > 100 and iteration < 125:
        radius -= 1
    elif iteration > 125 and iteration < 150:
        radius -= 2
    elif iteration > 150 and iteration < 175:
        radius -= 3
    elif iteration > 175 and iteration < 200:
        radius -= 4

    iteration += 1
    print(radius)

    pygame.draw.circle(screen, (255, 255, 255), (200, 200), radius)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
