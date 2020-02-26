def min_max(arr):
    if len(arr)> 0:
        min_number =arr[0]
        max_number = arr[0]
        for num in arr:
            if num < min_number:
                min_number = num
            if num > max_number:
                max_number = num
        return (min_number, max_number)
    else:
        return -1


arr = [15,5,4,3,99,7,11,45,1,9]
print("Pass" if min_max(arr)==(1,99) else "Fail")
print("Pass" if min_max([1,1])==(1,1) else "Fail")
print("Pass" if min_max([])== -1 else "Fail")