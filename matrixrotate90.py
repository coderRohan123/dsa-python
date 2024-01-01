def rotate(matrix):
    n = len(matrix)

    # Reverse the rows
    matrix.reverse()

    # Transpose the matrix in-place
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(rotate(matrix))

# The matrix will be rotated 90 degrees clockwise
# Result:
# [
#   [7, 4, 1],
#   [8, 5, 2],
#   [9, 6, 3]
# ]