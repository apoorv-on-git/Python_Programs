#Function to count the different cells in which a chess knight can move from the given direction with error handling
def chessKnight(cell):
    count = 0
    board = [[0 for i in range(0, 8)] for j in range (0, 8)]
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    column = alpha.index(cell[0])
    row = int(cell[1]) - 1
    try:
        element = board[row+2][column+1]
        count = count + 1
    except:
        pass
    try:
        element = board[row+2][column-1]
        if (column-1) < column and column < 1:
            pass
        else:
            count = count + 1
    except:
        pass
    try:
        element = board[row+1][column+2]
        count = count + 1
    except:
        pass
    try:
        element = board[row+1][column-2]
        if (column-2) < column and column < 2:
            pass
        else:
            count = count + 1
    except:
        pass
    try:
        element = board[row-1][column+2]
        if (row-1) < row and row < 1:
            pass
        else:
            count = count + 1
    except:
        pass
    try:
        element = board[row-1][column-2]
        if (row-1) < row and row < 1:
            pass
        elif (column-2) < column and column < 2:
            pass
        else:
            count = count + 1
    except:
        pass
    try:
        element = board[row-2][column+1]
        if (row-2) < row and row < 2:
            pass
        else:
            count = count + 1
    except:
        pass
    try:
        element = board[row-2][column-1]
        if (row-2) < row and row < 2:
            pass
        elif (column-1) < column and column < 1:
            pass
        else:
            count = count + 1
    except:
        pass
    return count
