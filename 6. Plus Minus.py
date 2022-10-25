def plusMinus(arr):
    n = len(arr)
    npositive = 0
    nnegative = 0
    nzero = 0
    
    for i in arr:
        if i>0:
            npositive += 1
        elif i<0:
            nnegative += 1
        else:
            nzero += 1
     
    print(round(npositive/n, 6))
    print(round(nnegative/n, 6)) 
    print(round(nzero/n, 6))

arr = [1,23,4,-5,6,-3,-5,0,0]
plusMinus(arr)