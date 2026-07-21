# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

def solution(arr):
    first = arr[0]
    length = len(first)
    for i in arr[1:]:
        while i[:length] != first:
            length -= 1
            first = first[:length]
            if first == "":
                return first
    return first


print(solution(["flower", "flow", "flight"]))
print(solution(["dog", "love", "flight"]))