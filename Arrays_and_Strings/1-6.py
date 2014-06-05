def transpose(matrix):
    print matrix
    lenth = len(matrix)
    for i in range(0, lenth):
        for j in range(i + 1, lenth):
            a = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = a

    print matrix


# this is actually the real question not transpose as implemented above
def rotate90(matrix):
    for row in matrix:
        print row

    # for more commented code read the book
    length = len(matrix)
    for layer in range(0, length / 2):
        # do the four way swap
        for i in range(layer, length - 1 - layer):
            top = matrix[layer][i]

            matrix[layer][i] = matrix[length - 1 - i][layer]
            matrix[length - 1 - i][layer] = matrix[layer][length - 1 - i]
            matrix[layer][length - 1 - i] = matrix[length - 1 - i][length - layer - 1]
            matrix[length - 1 - i][length - layer - 1] = top

            # top, right, bottom, left = left, top, right, bottom
            # matrix[layer][i], matrix[layer][length - 1 - i], matrix[length - 1 - i][length - layer - 1], matrix[length - 1 - i][layer] = matrix[length - 1 - i][layer], matrix[layer][i], matrix[layer][i], matrix[layer][i]

            print 'aa'

    for row in matrix:
        print row

rotate90([[i for i in range(1, 5)] for j in range(1, 5)])
