file_name = input("Enter the name of the file: ")
try:
    file = open(file_name, "r")
except:
    print("The file doesn't exist")
    
try:
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
    print("The number of unique senders are:",len(unique))
    print("The maximum no of emails are done by",key_list[index],"which is", max_email)

except:
    print("The file is empty.")
