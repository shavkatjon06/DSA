# Given a sorted array arr[] of size n, the goal is to rearrange the array so that all distinct elements appear at the beginning in sorted order. Additionally, return the length of this distinct sorted subarray.

def solution1(arr):
    bag = {}
    for num in arr:
        if num not in bag:
            bag[num] = True
    temp = []
    for key in bag.keys():
        temp.append(key)
    return {
        "arr": temp,
        "length": len(temp)
    }


print(solution1([2, 2, 2, 2, 2]))
print(solution1([1, 2, 2, 3, 4]))


def solution2(arr):
    idx = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            arr[idx] = arr[i]
            idx += 1
    return {
        "arr": arr[:idx],
        "length": idx
    }

print(solution2([2, 2, 2, 2, 2]))
print(solution2([1, 2, 2, 3, 4]))