#a = int(input("Enter the size of array: "))
b = input()
c = b.split(" ")
arr = []
for i in c:
    arr.append(int(i))

def SumOfArray(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum

sum = SumOfArray(arr)
print(sum)
