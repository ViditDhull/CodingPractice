try:
    file = open("mbox_short.txt", "r")
except:
    print("The file doesn't exist")
    

lines = file.readlines()
d = {}
unique = []
counts = []
for i in lines:
    i = i.split()
    if len(i) > 0:
        if i[0] == "From":
            counts.append(i[1])
            if i[1] not in unique:
                unique.append(i[1])
            d[i[1]] = counts.count(i[1])

key_list = list(d.keys())
val_list = list(d.values())
max_email = max(val_list)
index = val_list.index(max_email)
if len(lines) == 0:
    print("The file is empty.")
else:
    print("The number of unique senders are:",len(unique))
    print("The maximum no of emails are done by",key_list[index],"which is", max_email)
