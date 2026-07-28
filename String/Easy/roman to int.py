# Given a string s representing a Roman numeral, find it's corresponding integer value.

def solution(word):
    bag = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    result = 0
    for i in range(len(word)):
        if i+1 < len(word) and bag[word[i]] < bag[word[i+1]]:
            result -= bag[word[i]]
        else:
            result += bag[word[i]]
    return result


print(solution("I"))
print(solution("III"))
print(solution("IV"))
print(solution("V"))
print(solution("VII"))
print(solution("XI"))
print(solution("MD"))