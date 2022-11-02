def solve_expression(string):
    element = string.split()
    str1 = element[0]
    str2 = element[2]
    opr = element[1]
    if '.' in str1:
        num1 = float(str1)
    else:
        num1 = int(str1)
        
    if '.' in str2:
        num2 = float(str2)
    else:
        num2 = int(str2)
        
    if opr == "+":
        result = num1 + num2
    elif opr == "-":
        result = num1 - num2
    elif opr == "x":
        result = num1 * num2
    elif opr == "/":
        result = num1/num2
    elif opr == "^":
        result = num1 ** num2
    else:
        print("The operator is not supported.")
    
    strresult = str1 + " " + opr + ' ' + str2 + ' ' + "=" + " " + str(result)
    return strresult

listline = []
try:
    file = open("test.txt", "r")
    
except:
    print("File not Found.")
for line in file:
    listline.append(solve_expression(line) + "\n")
file.close()
file1 = open("result.txt", "w")
file1.writelines(listline)
file1.close()