"""4. Generate Pascal’s Triangle Up to a Given Row

Task:
Write a function to generate Pascal's Triangle up to the specified number of rows."""

def pascalTriangle(rows):
    # initializing triangle
    triangle = []
    for num in range(rows):
        triangle.append([1] * num)
    # every nth row numbers sum should add up to n^3
    # for i in range(len(triangle)):
    #     for j in range(len(i)):
    #         triangle[i][j] = triangle[i - 1][j] + triangle[i - 1][j + 1]
    # unfinished
    return triangle    


# Test Cases:
# 1. Input: 1 → Output: [[1]]
print(pascalTriangle(1))
# 2. Input: 2 → Output: [[1], [1, 1]]
print(pascalTriangle(2))
# 3. Input: 3 → Output: [[1], [1, 1], [1, 2, 1]]
print(pascalTriangle(3))
# 4. Input: 5 → Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6,
# 4, 1]]
print(pascalTriangle(5))
# 5. Input: 0 → Output: []
print(pascalTriangle(0))