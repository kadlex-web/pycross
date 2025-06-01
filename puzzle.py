import pygame #type:ignore

class Puzzle:
    def __init__(self):
        self.answer = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
                       ]
        
        self.rows = len(self.answer)
        self.columns = len(self.answer[0])
        self.name = "Test Puzzle"

    def row_clues(self):
        row_clue_list = []
        clue_value = 0
        for row in self.answer:
            for column in row:
                clue_value += column
            row_clue_list.append(clue_value)
            clue_value = 0
        return row_clue_list
    
    def column_clues(self):
        column_clue_list = []
        clue_value = 0
        for i in range(self.rows):
            for j in range(self.columns):
                clue_value += self.answer[j][i]
            column_clue_list.append(clue_value)
            clue_value = 0
        return column_clue_list