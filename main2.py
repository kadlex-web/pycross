import sys, pygame # type:ignore
from grid import Grid
from puzzle import Puzzle

pygame.init()
pygame.font.init()
size = 1024, 780
screen = pygame.display.set_mode(size)

def main_menu():
    while True:
        screen.fill("white")
        title_font = pygame.font.SysFont(None, 50)
        title_text = pygame.font.Font.render(title_font, "Start Puzzle", True, "black")
        tt_width, tt_height = title_text.get_size()
        title_button = pygame.Rect(200, 350, tt_width,tt_height)
        pygame.draw.rect(screen, "grey", title_button)
        screen.blit(title_text, (200, 350))

        for event in pygame.event.get():
            # listen for quit
            if event.type == pygame.QUIT: 
                pygame.exit()
                sys.exit()

            #listen for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    click_x = pygame.mouse.get_pos()[0]
                    click_y = pygame.mouse.get_pos()[1]

                    # if the user clicks the start button on the title -- the test puzzle should be loaded for the user to interact with
                    if pygame.Rect.collidepoint(title_button, click_x, click_y):
                        play()
        pygame.display.update()

def play():
    screen.fill("white")
    test_puzzle = Puzzle()
    grid = Grid(5,5, screen, test_puzzle)
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
                    
        grid._render()
        pygame.display.update() # Displays the new board

main_menu()