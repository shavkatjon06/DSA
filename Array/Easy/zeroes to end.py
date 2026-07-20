# Given an array of integers arr[], move all the zeros to the end of the array while maintaining the relative order of all non-zero elements.

def solution(arr):
    length = len(arr)
    pointer = 0
    for i in range(length):
        if arr[i] != 0:
            arr[pointer] = arr[i]
            pointer += 1
    for i in range(pointer, length):
        arr[i] = 0
    return arr


print(solution([1, 2, 0, 4, 0, 3]))