import pygame # type:ignore

class Cell:
    def __init__(self, left, top, width, height):
        # pygame.Rect stored inside each cell
        self.rect = pygame.Rect(left, top, width, height)
        # initial color the rectangle is drawn as
        self.color = "white"
        # initial toggle state
        self.toggle = 0
        # location of the cell in the grid
        self.location = None