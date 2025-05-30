import sys, pygame # type:ignore
from grid import Grid
from interface import Text
from puzzle import Puzzle

pygame.init()
size = width, height = 1024, 780
screen = pygame.display.set_mode(size)
screen.fill("white")
test_puzzle = Puzzle()
grid = Grid(5, 5, screen, test_puzzle)
screen.blit(Text.surface_text, (200,10))
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
                            cell.toggle = 1
                        elif cell.toggle:
                            cell.color = "white"
                            cell.toggle = 0
        # If user presses the 'A' key -- the puzzle will be checked. If a solution is found, the game exits
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                grid.check_puzzle()

    grid._render() # Renders the updated puzzle
    pygame.display.update() # Displays the new board