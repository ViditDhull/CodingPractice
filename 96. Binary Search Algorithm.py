def binary_search(num_lst, ele, left_index, right_index):
    if right_index < left_index:
        return -1
    
    mid_index = (left_index + right_index) // 2
    if mid_index >= len(num_lst) or mid_index < 0:
        return -1
    
    mid_number = num_lst[mid_index]

    if mid_number == ele:
        return mid_index
    
    if mid_number < ele:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search(num_lst, ele, left_index, right_index)