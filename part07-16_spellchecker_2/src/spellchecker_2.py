# # Write your solution here
# import difflib
# import os

# wt = input('Write text: ')
# word = ''
# words = []

# base_dir = os.path.dirname(__file__)
# file_path = os.path.join(DIR, "wordlist.txt")

# with open(file_path, encoding="utf-8") as new_file:
#     for line in new_file:
#         words.append(line.strip())

# parts = wt.split(' ')
# c = []
# for x in parts:
#     if x.lower() not in words:
#         word = x
#         x = '*' + x + '*'
#     c.append(x)
# result = difflib.get_close_matches(word,words)
# sentence = " ".join(c)
# print(sentence)
# print('suggestions : ')
# print(f'{word}: {', '.join(result)}')

import difflib
import os

# read input
text = input("Write text: ")

# load word list safely
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "wordlist.txt")

words = []
with open(file_path, encoding="utf-8") as f:
    for line in f:
        words.append(line.strip())

# spell check
parts = text.split()
marked = []
misspelled = []

for word in parts:
    if word.lower() not in words:
        marked.append(f"*{word}*")
        if word not in misspelled:
            misspelled.append(word)
    else:
        marked.append(word)

# print corrected sentence
print(" ".join(marked))

# print suggestions
print("suggestions:")
for word in misspelled:
    suggestions = difflib.get_close_matches(word.lower(), words)
    print(f"{word}: {', '.join(suggestions)}")
