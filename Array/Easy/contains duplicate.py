# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def solution1(arr):
    arr = sorted(arr)
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return True
    return False


print(solution1([1, 2, 3, 1]))
print(solution1([1, 2, 3, 4]))


def solution2(arr):
    bag = {}
    for i in arr:
        if i in bag:
            bag[i] += 1
        else:
            bag[i] = 1
    for key, val in bag.items():
        if val > 1:
            return True
    return False


print(solution2([1, 2, 3, 1]))
print(solution2([1, 2, 3, 4]))