count_dict = {}
with open(r"c:\Users\vidit\Downloads\poem.txt") as f:
    lines = f.readlines()
    for i in lines:
        tokens = i.split()
        for j in tokens:
            if j in count_dict.keys():
                count_dict[j] += 1
            else:
                count_dict[j] = 1

print(count_dict)