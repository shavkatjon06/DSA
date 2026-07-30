# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

def solution(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    left, right = 0, len(word) - 1
    temp = list(word)
    while left < right:
        while left < right and temp[left] not in vowels:
            left += 1
        while left < right and temp[right] not in vowels:
            right -= 1
        temp[left], temp[right] = temp[right], temp[left]
        left += 1
        right -= 1
    return ''.join(temp)


print(solution("leetcode"))
print(solution("hello"))