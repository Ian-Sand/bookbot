import string

with open('books/frankenstein.txt', 'r') as file:
    content = file.read()
    word_count = len(content.split())
    content_lower = content.lower()
    char_count = {char: content.count(char) for char in set(content) if char in string.ascii_lowercase}
    sorted_char_count = {k: v for k, v in sorted(char_count.items(), key=lambda item: item[1], reverse=True)}

    #print(word_count)
    #print(sorted_char_count)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for key, value in sorted_char_count.items():
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")