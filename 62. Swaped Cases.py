def swap_case(s):
    str_lst = []
    for i in s:
        if i.isupper():
            str_lst.append(i.lower())
        else:
            str_lst.append(i.upper())
    str_s = ''.join(str_lst)
    return str_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)