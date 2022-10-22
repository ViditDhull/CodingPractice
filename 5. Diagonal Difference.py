arr = [[1,2,3],[4,5,6],[7,8,9]]


def diagonalDifference(arr):
    sumr = arr[0][0] + arr[1][1] + arr[2][2]
    suml = arr[2][0] + arr[1][1] + arr[0][2]
    if sumr > suml:
        return sumr-suml
    elif suml > sumr:
        return suml-sumr
    else:
        return 0

print(diagonalDifference(arr))