def find_longest_word(words):
    longest_word = max(words, key=len)
    return longest_word, len(longest_word)

words = ["apple", "banana", "grapefruit", "kiwi", "blueberry"]
longest_word, length = find_longest_word(words)
print(f"Longest word: '{longest_word}', Length: {length}")
