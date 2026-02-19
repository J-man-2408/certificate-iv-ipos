# 2d list
two_dim_list_1 = [[1, 2, 3], [4, 5, 6],[7, 8]]

# Random access
print(two_dim_list_1[0][2])  


# Numpy & Pandas examples - view in Pycharm

import numpy as np
import pandas as pd

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) #This is a NumPy array (like a grid/matrix)

arr2 = arr * 2 # Instead of looping manually - NumPy applies *2 to all elements

# This creates a DataFrame (table with rows and columns)
df = pd.DataFrame({
    'A':[1,2,3], # A is the Key/column name, the list becomes the row
    'B':[4,5,6],
    'C':[7,8,9]
})

# Exercise 1a: manually create a 2D data structure

my_2dim_list = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

#Random access
print(my_2dim_list[0]) # Runs the first row
print(my_2dim_list[1][2]) # Finds the second rows third element (indexing starts at 0)

print('#'*20) # You can times strings

# Print all
for row in my_2dim_list: # Loops through rows
    for elem in row: # Loops though elements in that row
        print(elem, end=', ')
    print()

# Exercise 1b: Be careful when creating 2D data structures using multiplication

# row = [0, 1, 2]
# my_2dim_list = [row] * 3

# print("Before:", my_2dim_list)  # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# # Update one element in the first row
# my_2dim_list[0][0] = 99
# print(f"Row 1 location: {id(my_2dim_list[0])}")
# print(f"Row 2 location: {id(my_2dim_list[1])}")
# print(f"Row 3 location: {id(my_2dim_list[2])}")

# print("After:", my_2dim_list)   # [[99, 1, 2], [99, 1, 2], [99, 1, 2]] - WHAT!
# print('#'*20)

# Exercise 2: sequential iteration over 2D - aka sequential access

# for row in my_2dim_list:
#     for grid_square in row:
#         # check, change remove, set initial
#         print(grid_square)

# print('#'*20)

# Exercise 3: build a 2D data structure and initialise with values

print("END !!!!!", '#'*20)