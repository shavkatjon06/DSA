# Given two non-empty strings s1 and s2 of lowercase letters, determine if they are anagrams — i.e., if they contain the same characters with the same frequencies.

def solution(word1, word2):
    if len(word1) != len(word2):
        return False
    bag = {}
    for i in word1:
        if i in bag:
            bag[i] += 1
        else:
            bag[i] = 1
    for i in word2:
        if i not in bag:
            return False
        if i in bag:
            if bag[i] < 1:
                return False
            bag[i] -= 1
    return True


print(solution("listen", "list"))
print(solution("lemon", "melon"))
print(solution("save", "vase"))