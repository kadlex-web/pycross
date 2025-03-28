import pygame # type:ignore

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
        self._create_grid()

    def _create_grid(self):
        width = 100
        height = 100
        init_top = 100
        init_left = 100
        black = 0,0,0

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                r = pygame.Rect(100+(init_top*i), 100+(init_left*j), width, height)
                pygame.draw.rect(self._surface, black, r, width=1)