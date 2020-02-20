def sorted_array_search(input_list, target):
    start = 0
    end = len(input_list)-1
    while start<=end:
        mid = (start+end)//2
        mid_value = input_list[mid]
        start_value = input_list[start]
        end_value = input_list[end]
        if mid_value == target:
            return mid
        if mid_value < target:
            start = mid+1
        elif mid_value >target:
            end = mid-1
    return -1

def get_index(input, target):
    return return_get_index(input, target, 0, len(input)-1)
    
def return_get_index(input, target, start, end):
    if start > end:
        return -1
    mid = (start+end)//2
    if input[mid] == target:
        return mid
    if input[start] <= input[mid]:
        if target >= input[start] and target <= input[mid]:
            return return_get_index(input, target, start, mid-1)
        return return_get_index(input, target, mid+1, end)
    if target >= input[mid] and target <= input[end]:
        return return_get_index(input, target, mid+1, end)
    return return_get_index(input, target, start, mid-1)
    

print("Pass" if get_index([18,1,2,3,4,5,6,7,8], 1)== 1 else "Fail")
print("Pass" if get_index([2,4,5,7,8,9,1], 8) == 4 else "Fail")
print("Pass" if get_index([2,4,5,7,8,9,1], 3) == -1 else "Fail")
print("Pass" if get_index([21,31,41,1,11], 31) == 1 else "Fail")

