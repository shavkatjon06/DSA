# Given an array of positive integers arr[] of size n, the task is to find second largest distinct element in the array.


def secondLargest(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 0:
        return None
    largest = arr[0]
    secondLarge = -1
    for i in range(1, len(arr)):
        if arr[i] > largest:
            secondLarge = largest
            largest = arr[i]
        if largest > arr[i] > secondLarge:
            secondLarge = arr[i]
    return {
        "largest": largest,
        "secondLarge": secondLarge
    }


print(secondLargest([12, 35, 1, 10, 34, 11]))
