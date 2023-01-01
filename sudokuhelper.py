import numpy as np
import pandas as pd
import math

class Sudoku:
    def __init__(self,*args):
        if len(args) == 0:
            self.genrandom_sudoku()
        else:
            array = args[0]
            self.array = array
    
    def genrandom_sudoku(self):
        self.array = np.random.randint(0,10,size = (9,9)).astype('float64')
        self.array[self.array == 0] = np.nan
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
        if k not in range(1,10):
            print("Index out of range")
        else:
            x , y = (k-1)//3 , (k-1)%3 
            return self.array[3*x:3*x+3,3*y:3*y+3]
    
    def is_box_valid(self,k):
        box = self.get_box(k)
        L = []
        for row in box:
            for j in row:
                L.append(j)
        for x in L:
            if not math.isnan(x):
                if int(x) not in [1,2,3,4,5,6,7,8,9]:
                    return False
                elif L.count(x) > 1:
                    return False
                else:
                    continue
            else:
                continue
        else:
            return True
    
    def is_sudoku_valid(self):
        for k in range(1,10):
            if not self.is_box_valid(k):
                return False
            if not self.is_col_valid(k):
                return False
            if not self.is_row_valid(k):
                return False
        else:
            return True

# arr = np.array([[np.nan,np.nan,np.nan,np.nan,8,np.nan,np.nan,4,np.nan],[8,np.nan,1,np.nan,6,9,np.nan,np.nan,np.nan]])
# print(list(arr[0]))    

# s1 = Sudoku(arr)
# print(s1.is_row_valid(0))

while True:
    sudo = Sudoku()
    print(sudo.array)
    print("_"*10)
    x = sudo.is_sudoku_valid()
    print(x)
    if x:
        break