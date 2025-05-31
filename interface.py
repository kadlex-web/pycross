import pygame # type:ignore
from puzzle import Puzzle

# Creates a timer showing how much time has passed since the puzzle began
class Clock:
    pass

# Creates a Text object which is used to display text on the surface window
class Text:
    pygame.font.init()
    font = pygame.font.SysFont(None, 100)
    text = "Puzzle 1"
    surface_text = pygame.font.Font.render(font, text, True, "black")

class Title_Screen:
    def __init__(self):
        pygame.font.init()
        font = pygame.font.SysFont(None, 100)
        text = "Start Puzzle"
        pygame.font.Font.render(font, text, True, "black")