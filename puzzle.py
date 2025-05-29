import pygame #type:ignore

class Puzzle:
    def __init__(self):
        self.answer = [
            [1,1,1,1,1],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
                       ]
        self.name = "Test Puzzle"