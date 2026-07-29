# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def solution(word, target):
    for i in range(len(word)):
        if word[i:len(target)+i] == target:
            return i
    return -1


print(solution("sadbutsad", "sad"))
print(solution("code", "code"))
print(solution("leetcode", "leeto"))