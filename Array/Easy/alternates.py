# Given an array arr[], the task is to print every alternate element of the array starting from the first element.

def solution(arr):
    for i in range(0, len(arr), 2):
        print(arr[i])
    return


solution([1, 2, 3, 4, 5])
