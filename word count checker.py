def count_word_frequency(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
words=["apple","banana","apple","orange","banana","apple","pine"]
print(count_word_frequency(words))
'''This function counts the frequency of each word in a list of words and returns
  them as an array.'''