
def msquares(squares):
    """magic quares example 
    [
        [4, 9, 2],
        [3, 5, 7],
        [8, 1, 6]
    ]
    Args:
        squares (mxm list): square of multidimentional metrics
    """
    sum_rows = []
    sum_colum = dict()
    for i in range(len(squares)):
        sum_rows.append(0)
        sum_colum[i] = 0

    sum_diag = 0
  
    j = 0
    rsums = 0
    for i in range(len(squares)):
        
        for j in range(len(squares)):
            rsums = rsums + squares[i][j]
            sum_colum[j] = sum_colum[j] + squares[i][j]

            if i  == j :
                sum_diag = sum_diag + squares[i][j]

        sum_rows[i] = rsums
        rsums = 0

    return sum_colum.values(), sum_rows, sum_diag
msq = [
        [4, 9, 2],
        [3, 5, 7],
        [8, 1, 6]

    ]

print(msquares(msq))
