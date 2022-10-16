a = input()
b = input()

astr = a.split(" ")
bstr = b.split(" ")
arr = []
brr = []
for i in astr:
    arr.append(i)

for j in bstr:
    brr.append(j)

def compare(arr, brr):
    suma = 0
    sumb = 0
    for i in range(3):
        if a[i] > b[i]:
            suma += 1
        elif a[i] < b[i]:
            sumb += 1
    result = []
    result.append(suma)
    result.append(sumb)
    return result


result = compare(arr, brr)
print(result)