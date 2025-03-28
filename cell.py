import pygame # type:ignore

class Cell(pygame.Rect):
    def __init__(self, top, left, width, height):
        self._top = top
        self._left = left
        self._width = width
        self.height = height
        