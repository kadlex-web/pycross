import sys, pygame # type:ignore
from grid import Grid

pygame.init()
size = width, height = 700, 700
screen = pygame.display.set_mode(size)
screen.fill("white")
grid = Grid(5, 5, screen)
grid._render()

while True:
    for event in pygame.event.get():
        # listen for quit
        if event.type == pygame.QUIT: 
            sys.exit()
        #listen for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                click_x = pygame.mouse.get_pos()[0]
                click_y = pygame.mouse.get_pos()[1]

                for cell in grid.cell_list:
                    if pygame.Rect.collidepoint(cell.rect, click_x, click_y):
                        if not cell.toggle:
                            cell.color = "gray"
                            cell.toggle = True
                        elif cell.toggle:
                            cell.color = "white"
                            cell.toggle = False

    grid._render() # Renders the updated puzzle
    pygame.display.update() # Displays the new board