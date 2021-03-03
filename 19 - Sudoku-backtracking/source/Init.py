'''
Created on 21/01/2021
@author: VATS
'''
from pandas.core.indexes.interval import _is_valid_endpoint
from _abc import __name__

def find_next_empty(puzzle):
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == 0 :
                return row, column
    
    return None, None
       
def is_valid(puzzle, guess, row, column):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    #col_vals = []
    #for i in range(9):
    #   column.append(puzzle[i][column])
    col_vals = [puzzle[i][column] for i in range(9)]
    if guess in col_vals:
        return False
    
    row_start = (row // 3) * 3
    col_start = (column // 3) * 3
    
    for r in range(row_start, row_start + 3):
        for col in range(col_start, col_start + 3):
            if puzzle[r][col] == guess :
                return False
    
    return True
   
   
    
def solve_sudoku(puzzle):
    
    row, column = find_next_empty(puzzle)
    if row is None:
        return True
    for guess in range(1,10):
        if is_valid(puzzle, guess, row, column):
            puzzle[row][column] = guess
            
            if solve_sudoku(puzzle):
                return True
            #BackTrack and try again
        puzzle[row][column] = 0
    return False
            

import numpy as np

#print("Hola")
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]
print(solve_sudoku(grid))
print(np.matrix(grid))