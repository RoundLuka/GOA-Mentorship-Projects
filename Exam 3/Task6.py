"""6. Validate a Sudoku Solution

Task Explanation:
Write a function that validates whether a given Sudoku board is
solved correctly. The board is represented as a 2D array of size
9x9. A valid solution must meet these conditions:
1. Each row contains numbers 1–9 without repetition.
2. Each column contains numbers 1–9 without repetition.
3. Each 3x3 subgrid contains numbers 1–9 without repetition."""

def sudoku(matrix):
    # initialized instance of tranposed matrix where each row has to represent column of old matrix
    transposed_matrix = [
        ["0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0"]
    ]
    # first checking rows for duplicate numbers
    for row in matrix:
        for num in row:
            if row.count(num) > 1:
                return False
    # logic to swap matrix and turn each row into column
    for col in range(9):
        for rowline in range(9):
            transposed_matrix[col][rowline] = matrix[rowline][col]
    # easily checking columns of original matrix (rows for this one) as if they were rows, checking if there are duplicate numbers
    for row in transposed_matrix:
        for num in row:
            if row.count(num) > 1:
                return False
    return True



# Test Cases:
# 1. Valid
# Input:
# [
# [5, 3, 4, 6, 7, 8, 9, 1, 2],
# [6, 7, 2, 1, 9, 5, 3, 4, 8],
# [1, 9, 8, 3, 4, 2, 5, 6, 7],
# [8, 5, 9, 7, 6, 1, 4, 2, 3],
# [4, 2, 6, 8, 5, 3, 7, 9, 1],
# [7, 1, 3, 9, 2, 4, 8, 5, 6],
# [9, 6, 1, 5, 3, 7, 2, 8, 4],
# [2, 8, 7, 4, 1, 9, 6, 3, 5],
# [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ]
# Expected Output: True
print(sudoku([
[5, 3, 4, 6, 7, 8, 9, 1, 2],
[6, 7, 2, 1, 9, 5, 3, 4, 8],
[1, 9, 8, 3, 4, 2, 5, 6, 7],
[8, 5, 9, 7, 6, 1, 4, 2, 3],
[4, 2, 6, 8, 5, 3, 7, 9, 1],
[7, 1, 3, 9, 2, 4, 8, 5, 6],
[9, 6, 1, 5, 3, 7, 2, 8, 4],
[2, 8, 7, 4, 1, 9, 6, 3, 5],
[3, 4, 5, 2, 8, 6, 1, 7, 9]
]))
# 2. Invalid Board with Duplicate in a Row
# Input:
# [
# [5, 3, 4, 6, 7, 8, 9, 1, 2],
# [6, 7, 2, 1, 9, 5, 3, 4, 8],
# [1, 9, 8, 3, 4, 2, 5, 6, 7],
# [8, 5, 9, 7, 6, 1, 4, 2, 3],
# [4, 2, 6, 8, 5, 3, 7, 9, 1],
# [7, 1, 3, 9, 2, 4, 8, 5, 6],
# [9, 6, 1, 5, 3, 7, 2, 8, 4],
# [2, 8, 7, 4, 1, 9, 6, 3, 5],
# [3, 4, 5, 2, 8, 6, 1, 7, 7] # Invalid: Two 7s in the last row
# ]
# Expected Output: False
print(sudoku([
[5, 3, 4, 6, 7, 8, 9, 1, 2],
[6, 7, 2, 1, 9, 5, 3, 4, 8],
[1, 9, 8, 3, 4, 2, 5, 6, 7],
[8, 5, 9, 7, 6, 1, 4, 2, 3],
[4, 2, 6, 8, 5, 3, 7, 9, 1],
[7, 1, 3, 9, 2, 4, 8, 5, 6],
[9, 6, 1, 5, 3, 7, 2, 8, 4],
[2, 8, 7, 4, 1, 9, 6, 3, 5],
[3, 4, 5, 2, 8, 6, 1, 7, 7] 
]))
# 3. Invalid Board with Duplicate in a Column
# Input:
# [
# [5, 3, 4, 6, 7, 8, 9, 1, 2],
# [6, 7, 2, 1, 9, 5, 3, 4, 8],
# [1, 9, 8, 3, 4, 2, 5, 6, 7],
# [8, 5, 9, 7, 6, 1, 4, 2, 3],
# [4, 2, 6, 8, 5, 3, 7, 9, 1],
# [7, 1, 3, 9, 2, 4, 8, 5, 6],
# [9, 6, 1, 5, 3, 7, 2, 8, 4],
# [2, 8, 7, 4, 1, 9, 6, 3, 5],
# [3, 4, 5, 2, 8, 6, 9, 7, 9] # Invalid: Two 9s in the last
# column
# ]
print(sudoku([
[5, 3, 4, 6, 7, 8, 9, 1, 2],
[6, 7, 2, 1, 9, 5, 3, 4, 8],
[1, 9, 8, 3, 4, 2, 5, 6, 7],
[8, 5, 9, 7, 6, 1, 4, 2, 3],
[4, 2, 6, 8, 5, 3, 7, 9, 1],
[7, 1, 3, 9, 2, 4, 8, 5, 6],
[9, 6, 1, 5, 3, 7, 2, 8, 4],
[2, 8, 7, 4, 1, 9, 6, 3, 5],
[3, 4, 5, 2, 8, 6, 9, 7, 9] 
]))
# Expected Output: False
# 4. Invalid Board with Duplicate in a 3x3 Subgrid
# Input:
# [
# [5, 3, 4, 6, 7, 8, 9, 1, 2],
# [6, 7, 2, 1, 9, 5, 3, 4, 8],
# [1, 9, 8, 3, 4, 2, 5, 6, 7],
# [8, 5, 9, 7, 6, 1, 4, 2, 3],
# [4, 2, 6, 8, 5, 3, 7, 9, 1],
# [7, 1, 3, 9, 2, 4, 8, 5, 6],
# [9, 6, 1, 5, 3, 7, 2, 8, 4],
# [2, 8, 7, 4, 1, 9, 6, 3, 5],
# [3, 4, 5, 2, 8, 6, 1, 1, 9] # Invalid: Two 1s in the
# bottom-right subgrid
# ]
print(sudoku([
[5, 3, 4, 6, 7, 8, 9, 1, 2],
[6, 7, 2, 1, 9, 5, 3, 4, 8],
[1, 9, 8, 3, 4, 2, 5, 6, 7],
[8, 5, 9, 7, 6, 1, 4, 2, 3],
[4, 2, 6, 8, 5, 3, 7, 9, 1],
[7, 1, 3, 9, 2, 4, 8, 5, 6],
[9, 6, 1, 5, 3, 7, 2, 8, 4],
[2, 8, 7, 4, 1, 9, 6, 3, 5],
[3, 4, 5, 2, 8, 6, 1, 1, 9] 
]))
# Expected Output: False
# 5. Partially Filled Board
# Input:
# [
# [5, 3, 0, 0, 7, 0, 0, 0, 0],
# [6, 0, 0, 1, 9, 5, 0, 0, 0],
# [0, 9, 8, 0, 0, 0, 0, 6, 0],
# [8, 0, 0, 0, 6, 0, 0, 0, 3],
# [4, 0, 0, 8, 0, 3, 0, 0, 1],
# [7, 0, 0, 0, 2, 0, 0, 0, 6],
# [0, 6, 0, 0, 0, 0, 2, 8, 0],
# [0, 0, 0, 4, 1, 9, 0, 0, 5],
# [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]
# Expected Output: False (Not completely filled, so cannot validate)
print(sudoku([
[5, 3, 0, 0, 7, 0, 0, 0, 0],
[6, 0, 0, 1, 9, 5, 0, 0, 0],
[0, 9, 8, 0, 0, 0, 0, 6, 0],
[8, 0, 0, 0, 6, 0, 0, 0, 3],
[4, 0, 0, 8, 0, 3, 0, 0, 1],
[7, 0, 0, 0, 2, 0, 0, 0, 6],
[0, 6, 0, 0, 0, 0, 2, 8, 0],
[0, 0, 0, 4, 1, 9, 0, 0, 5],
[0, 0, 0, 0, 8, 0, 0, 7, 9]
]))