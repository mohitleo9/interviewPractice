def clearLines(matrix):
    for row in matrix:
        print row
    clearRow = {}
    clearColumn = {}

    length = len(matrix)
    lengthc = len(matrix[0])

    for row in range(0, length):
        for col in range(0, lengthc):
            if matrix[row][col] == 0:
                clearRow[row] = True
                clearColumn[col] = True

    for row in range(0, length):
        for col in range(0, lengthc):
            if row in clearRow or col in clearColumn:
                matrix[row][col] = 0

    for row in matrix:
        print row


clearLines([
    [1, 0, 3],
    [1, 1, 1],
    [1, 1, 1],
    ])
