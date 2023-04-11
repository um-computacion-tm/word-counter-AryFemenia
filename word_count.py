def count_words(words):
    text = words.split()
    word_count = {}
    for word in text:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
