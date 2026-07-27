# Given a string s, the task is to check if it is palindrome or not.

def solution1(word):
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True


print(solution1("abba"))
print(solution1("abcd"))


def solution2(word):
    return word == word[::-1]


print(solution2("abba"))
print(solution2("abcd"))