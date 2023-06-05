if __name__ == '__main__':
    n_student = int(input())
    nm_list = []
    
    for i in range(n_student):
        each_record = []
        for j in range(2):
            inp = input()
            if j == 0:
                each_record.append(inp)
            else:
                each_record.append(float(inp))
        nm_list.append(each_record)
    
    nm_dict = {}
    for i in range(len(nm_list)):
        nm_dict[nm_list[i][0]] = nm_list[i][1]
    
    marks_list = []
    for i in range(len(nm_list)):
        marks_list.append(nm_dict[nm_list[i][0]])
    min_marks = min(marks_list)
    marks_list2 = []
    for i in marks_list:
        if i != min_marks:
            marks_list2.append(i)
    
    second_min_marks = min(marks_list2)
    
    names = []
    for i in nm_dict:
        if nm_dict[i] == second_min_marks:
            names.append(i)
    
    names.sort()
    for i in names:
        print(i)