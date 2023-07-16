if __name__ == '__main__':
    N = int(input())
    my_list = []

    for _ in range(N):
        command, *args = input().split()

        if command == 'insert':
            index = int(args[0])
            element = int(args[1])
            my_list.insert(index, element)
        elif command == 'print':
            print(my_list)
        elif command == 'remove':
            element = int(args[0])
            my_list.remove(element)
        elif command == 'append':
            element = int(args[0])
            my_list.append(element)
        elif command == 'sort':
            my_list.sort()
        elif command == 'pop':
            my_list.pop()
        elif command == 'reverse':
            my_list.reverse()
