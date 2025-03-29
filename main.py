import sys, pygame #type:ignore
from grid import Grid

pygame.init()
size = width, height = 1024, 768
screen = pygame.display.set_mode((1280,720))
screen.fill("white")
grid = Grid(5, 5, screen)
print(grid.cell_list)
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
                print(f"you click x:{click_x} and y:{click_y}")

                for cell in grid.cell_list:
                    if pygame.Rect.collidepoint(cell.rect, click_x, click_y):
                        if not cell.toggle:
                            pygame.draw.rect(screen, "black", cell.rect)
                            cell.toggle = True
                        else:
                            pygame.draw.rect(screen, "white", cell.rect)
                            cell.toggle = False
    # Need to redraw borders after the update
    pygame.display.flip()