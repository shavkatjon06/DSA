# Reverse an array arr[].

def solution1(arr):
    temp = []
    for i in range(len(arr)):
        temp.append(arr.pop())
    return temp


print(solution1([1, 2, 3, 4, 5]))


def solution2(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


print(solution2([1, 2, 3, 4, 5]))