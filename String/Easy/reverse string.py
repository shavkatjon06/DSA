# Given a string s, reverse the string. Reversing a string means rearranging the characters such that the first character becomes the last, the second character becomes second last and so on.

def solution1(word):
    temp = ""
    for i in range(len(word)-1, -1, -1):
        temp += word[i]
    return temp


print(solution1("hello"))


def solution2(word):
    return word[::-1]


print(solution2("hello"))