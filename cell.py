import pygame # type:ignore

class Cell():
    def __init__(self, left, top, width, height):
        self.rect = pygame.Rect(left, top, width, height)
        self.toggle = False