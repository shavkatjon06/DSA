# Given a character ch and a string s, the task is to find the index of the first occurrence of the character in the string. If the character is not present in the string, return -1.

def solution1(word, character):
    for idx, char in enumerate(word):
        if char == character:
            return idx
    return -1


print(solution1("book", "d"))
print(solution1("book", "k"))


def solution2(word, character):
    idx = word.find(character)
    return idx


print(solution2("apple", "e"))
print(solution2("apple", "o"))