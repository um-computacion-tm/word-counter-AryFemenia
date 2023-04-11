def count_letters(word):
    result = {}
    for letter in word.lower():
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result
