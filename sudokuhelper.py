import numpy as np
import pandas as pd
import math

class Sudoku:
    def __init__(self,array):
        self.array = array
    def get_row(self,i):
        return self.array[i]
    def get_col(self,j):
        return self.array[:,j]
    def is_row_valid(self,i): #checks if row follows sudoku rules
        row = list(self.get_row(i))
        for x in row:
            if not math.isnan(x):
                if int(x) not in [1,2,3,4,5,6,7,8,9]:
                    return False
                elif row.count(x) > 1:
                    return False
                else:
                    continue
            else:
                continue
        else:
            return True
            
    def is_col_valid(self,j): #checks if column follows sudoku rules
        col = list(self.get_col(j))
        for x in col:
            if not math.isnan(x):
                if int(x) not in [1,2,3,4,5,6,7,8,9]:
                    return False
                elif col.count(x) > 1:
                    return False
                else:
                    continue
            else:
                continue
        else:
            return True
    
    def get_box(self,k):
    

arr = np.array([[np.nan,np.nan,np.nan,np.nan,8,np.nan,np.nan,4,np.nan],[8,np.nan,1,np.nan,6,9,np.nan,np.nan,np.nan]])
print(list(arr[0]))    

s1 = Sudoku(arr)
print(s1.is_row_valid(0))