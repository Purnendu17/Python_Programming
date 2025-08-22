input_string = "madam level racecar kayak refer notapalindrome"
words = input_string.split()
find_palindromes = lambda word_list: list(filter(lambda word: word == word[::-1], word_list))
palindromes = find_palindromes(words)
print(f"Palindromes: {palindromes}")
