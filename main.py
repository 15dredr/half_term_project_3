import pygame

pygame.init()
DISPLAY = pygame.display.set_mode((800, 600))
FPSCLOCK = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
left_edge = 50
top = 50
width = 10
height = 40

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    DISPLAY.fill(black)
    pygame.draw.rect(DISPLAY, white, (left_edge, top, width, height))
    left_edge += 5
    pygame.display.update()
    FPSCLOCK.tick(30)
