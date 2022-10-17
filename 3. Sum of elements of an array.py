size = int(input("Enter the number of elements. "))
arr = []

for i in range(size):
    ele = int(input("Enter the element."))
    arr.append(ele)

def SumOfArray(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum

sum = SumOfArray(arr)
print("The sum of the array is", sum)