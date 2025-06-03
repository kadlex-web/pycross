import pygame #type:ignore

class Puzzle:
    def __init__(self):
        self.answer = [
            [1,0,1,0,1],
            [0,1,1,0,1],
            [1,1,0,1,1],
            [0,0,1,1,1],
            [1,0,0,1,1]
                       ]
        
        self.rows = len(self.answer)
        self.columns = len(self.answer[0])
        self.name = "Test Puzzle"

    # Generate a list of lists that correspond to the row clues that need to be printed on the puzzle
    def row_clues(self):
        row_clue_lists = []

        for row in self.answer:
            clue_list = []
            clue_value = 0

            for value in row:
                # If the current square is not filled and the current sequential values is 0; reset the counter and dont append it
                if value == 0 and clue_value == 0:
                    clue_value = 0
                # If the current square is not filled and the current sequential value is over 0; append the clue to the list and reset the counter
                elif value == 0 and clue_value > 0:
                    clue_list.append(clue_value)
                    clue_value = 0
                # otherwise simply add the value to the clue value
                clue_value += value
            # Check the final clue_value. If it's greater than 0, append it otherwise ignore it
            if clue_value != 0:
                clue_list.append(clue_value)
            # Takes the list of clues in the row and appends it to the master list
            row_clue_lists.append(clue_list)

        return row_clue_lists
    
    # Generate a list of lists that correspond to the column clues that need to be printed on the puzzle    
    def column_clues(self):
        column_clue_lists = []
    
        for i in range(self.rows):
            clue_list = []
            clue_value = 0

            for j in range(self.columns):
                value = self.answer[j][i]
                if value == 0 and clue_value == 0:
                    clue_value = 0
                elif value == 0 and clue_value > 0:
                    clue_list.append(clue_value)
                    clue_value = 0
                clue_value += value

            if clue_value != 0:
                clue_list.append(clue_value)

            column_clue_lists.append(clue_list)

        return column_clue_lists