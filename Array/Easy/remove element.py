# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

def solution(arr, k):
    idx = 0
    for i in arr:
        if i != k:
            arr[idx] = i
            idx += 1
    return idx


print(solution([3, 2, 2, 3], 3))
print(solution([0, 1, 2, 2, 3, 0, 4, 2], 2))
