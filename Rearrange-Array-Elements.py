def merge(list1, list2):
    l1 = 0
    l2 = 0
    result = list()
    while l1< len(list1) and l2 <len(list2):
        if list1[l1] < list2[l2]:
            result.append(list1[l1])
            l1 += 1
        else:
            result.append(list2[l2])
            l2 += 1
    result += list1[l1:]
    result += list2[l2:]
    return result

def rearrange(arr): #mergeSort
    if len(arr) <= 1:
        return arr
    start = 0
    end = len(arr) -1
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = rearrange(left)
    right = rearrange(right)

    return merge(left, right)

def getMaxSum(arr):
    arr = rearrange(arr)
    digit = len(arr)-1
    num1 = ""
    num2 = ""
    while digit >= 0:
        if digit%2 == 0:
            num1 += str(arr[digit])
        else:
            num2 += str(arr[digit])
        digit -= 1 

    return (num1, num2)


