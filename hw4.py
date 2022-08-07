def search_in_sorted_matrix(matrix, target):
    COLUMN = len(matrix[0]) - 1
    ROW = 0

    while ROW < len(matrix) and COLUMN >= 0:
        if matrix[ROW][COLUMN] > target:
            COLUMN -= 1
        elif matrix[ROW][COLUMN] < ROW:
            ROW += 1
        else:
            return [ROW, COLUMN]
    return [-1, -1]