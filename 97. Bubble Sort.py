def bubble_sort(elements):
    size = len(elements)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1): #need to go till last second element only
            if elements[i] > elements[i+1]:
                elements[i], elements[i+1] = elements[i+1], elements[i]
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    elements = [5, 9, 2, 1, 67, 34, 88, 34]

    bubble_sort(elements)
    print(elements)