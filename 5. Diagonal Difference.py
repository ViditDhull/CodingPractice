arr = [[1,2,3],[4,5,6],[7,8,9]]


def diagonalDifference(arr):
    sumr = 0
    suml = 0
    for i in range(n):
        sumr = sumr + arr[i][i]
    for i in range(n):
        suml = suml + arr[n-i-1][i]
    if sumr > suml:
        return (sumr) - (suml)
    elif suml > sumr:
        return (suml)-(sumr)
    else:
        return 0

print(diagonalDifference(arr))