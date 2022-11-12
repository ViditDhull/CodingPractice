import matplotlib.pyplot as plt

file_name = input("Enter the name of the file: ")
try:
    file = open(file_name, "r")
except:
    print("The file doesn't exist")
    
lines = file.readlines()
if len(lines) > 0:
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    counts = [0,0,0,0,0,0,0]
    for i in lines:
        if "X-DSPAM-Processed:" in i:
            if i[19:22] == "Sun":
                counts[0] = counts[0] + 1
            elif i[19:22] == "Mon":
                counts[1] = counts[1] + 1
            elif i[19:22] == "Tue":
                counts[2] = counts[2] + 1
            elif i[19:22] == "Wed":
                counts[3] = counts[3] + 1
            elif i[19:22] == "Thu":
                counts[4] = counts[4] + 1
            elif i[19:22] == "Fri":
                counts[5] = counts[5] + 1
            elif i[19:22] == "Sat":
                counts[6] = counts[6] + 1
            else:
                print('Error')
    plt.bar(week, counts, width = 0.6)
    plt.xticks(week, fontsize=8)
    plt.show()
    
else:
    print("The file is empty.")