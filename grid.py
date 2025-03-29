import pygame # type:ignore
from cell import Cell

# Creates and builds the grid object
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

    # Builds a grid object filled with Cell objects
    def _create_grid(self):
        width = 100
        height = 100
        init_top = 100
        init_left = 100

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                cell = Cell(100+(i*init_top), 100+(j*init_left), width, height)
                self.cell_list.append(cell)
                pygame.draw.rect(self._surface, "black", cell.rect, width=1)