import numpy as np

def rotate(image):
    N = len(image)

    # Step 1: Transpose the matrix (swap image[i][j] with image[j][i])
    for i in range(N):
        for j in range(i, N):  # j starts from i to avoid duplicate swaps
            image[i][j], image[j][i] = image[j][i], image[i][j]

    # Step 2: Reverse each row
    for i in range(N):
        image[i].reverse()

    return image

def rotate_counter_clockwise(matrix):
    N = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(N):
        for j in range(i, N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each column
    for j in range(N):
        for i in range(N // 2):
            matrix[i][j], matrix[N - 1 - i][j] = matrix[N - 1 - i][j], matrix[i][j]

    return matrix
