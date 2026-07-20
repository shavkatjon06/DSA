# right rotation

def solution1(arr):
    length = len(arr)
    last = arr[length - 1]
    for i in range(length-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = last
    return arr


print(solution1([1, 2, 3, 4, 5]))


# left rotation

def solution2(arr):
    length = len(arr)
    first = arr[0]
    for i in range(length-1):
        arr[i] = arr[i+1]
    arr[-1] = first
    return arr


print(solution2([1, 2, 3, 4, 5]))