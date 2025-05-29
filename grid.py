import pygame # type:ignore
from cell import Cell

# Creates and builds the Grid object
class Grid:
    def __init__(self, num_cols, num_rows, surface=None):
        # Number of columns the grid has
        self._num_cols = num_cols
        # Num of rows the grid has
        self._num_rows = num_rows
        # If not none, the screen that the grid will be initialized on
        self._surface = surface
        # builds and initializes the grid object
        self.cell_list = []
        self._create_grid()

    # Builds a Grid object which creates the visual boundaries of the puzzle
    def _create_grid(self):
        width = 100
        height = 100
        init_top = 100
        init_left = 100

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                box = pygame.Rect(100+(i*init_top), 100+(j*init_left), width, height)
                if j == (self._num_rows-1) and i == (self._num_cols-1):
                    cell = Cell(102+(i*init_top), 102+(j*init_left), width-4, height-4)
                elif i == (self._num_cols-1):
                    cell = Cell(102+(i*init_top), 102+(j*init_left), width-4, height-2)
                elif j == (self._num_rows-1):
                    cell = Cell(102+(i*init_top), 102+(j*init_left), width-2, height-4)
                else:
                    cell = Cell(102+(i*init_top), 102+(j*init_left), width-2, height-2)
                self.cell_list.append(cell)
                pygame.draw.rect(self._surface, "black", box, 2)

    # Renders the Cell objects on the pygame.Surface
    def _render(self):
        for cell in self.cell_list:
            pygame.draw.rect(self._surface, color=cell.color, rect=cell)
