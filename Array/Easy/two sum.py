# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

def solution(arr, target):
    bag = {}
    for idx, num in enumerate(arr):
        diff = target - num
        if diff in bag:
            return [bag[diff], idx]
        bag[num] = idx
    return False


print(solution([2, 7, 11, 15], 9))
print(solution([3, 2, 4], 6))