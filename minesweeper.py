#Function defined for the backend of minesweeper of any dimension
def minesweeper(matrix):
    height = len(matrix)
    width = len(matrix[0])
    result = [[0 for i in range(width)] for j in range(height)]
    for i in range(height):
        for j in range(width):
            if matrix[i][j]==True:
                if i>=1:
                    result[i-1][j]+=1
                    if j>=1:
                        result[i-1][j-1]+=1
                    if j<(width-1):
                        result[i-1][j+1]+=1
                if i<(height-1):
                    result[i+1][j]+=1
                    if j>=1:
                        result[i+1][j-1]+=1
                    if j<(width-1):
                        result[i+1][j+1]+=1
                if j>=1:
                    result[i][j-1]+=1
                if j<(width-1):
                    result[i][j+1]+=1
    return(result)
