# O(w*h) time | O(w*h) space
# w,h : width and height of the matrix
def transposeMatrix(matrix):
    transposedMatrix = []
    for column in range(len(matrix[0])):
        newRow = []
        for row in range(len(matrix)):
            newRow.append(matrix[row][column])
        transposedMatrix.append(newRow)
    return transposedMatrix