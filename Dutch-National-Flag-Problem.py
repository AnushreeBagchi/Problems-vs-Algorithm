def sort_012(arr):
    pivot_index = len(arr)-1
    start_index = 0
    end_index = len(arr)-1
    
    while pivot_index >= start_index:
        pivot_value = arr[pivot_index]
        if pivot_value == 0:
            start_value = arr[start_index]
            arr[start_index] = 0
            arr[pivot_index] = start_value
            start_index += 1
        elif pivot_value == 2:
            end_value = arr[end_index]
            arr[end_index] = 2
            arr[pivot_index] = end_value
            end_index -= 1
            pivot_index -= 1
        else:
            pivot_index -= 1

    return arr


def test_function(test_case):
    sorted_array = sort_012(test_case)
    # print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])



