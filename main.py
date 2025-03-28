import sys, pygame #type: ignore
from grid import Grid

pygame.init()
size = width, height = 800,600
white = 255, 255, 255
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        # listen for quit
        if event.type == pygame.QUIT: sys.exit()
        #listen for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("you clicked")
    screen.fill(white)
    grid = Grid(2, 2, screen)
    pygame.display.flip()