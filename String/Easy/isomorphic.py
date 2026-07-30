# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

def solution(word1, word2):
    if len(word1) != len(word2):
        return False
    bag1 = {}
    bag2 = {}
    for i in range(len(word1)):
        char1, char2 = word1[i], word2[i]
        if (char1 in bag1 and bag1[char1] != char2) or (char2 in bag2 and bag2[char2] != char1):
            return False
        else:
            bag1[char1] = char2
            bag2[char2] = char1
    return True


print(solution("egg", "add"))
print(solution("foo", "bar"))
print(solution("ba", "aa"))