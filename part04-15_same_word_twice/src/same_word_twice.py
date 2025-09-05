# Write your solution here
lst = []
while True:
    word = input('word: ')
    if word in lst:
        break
    else:
      lst.append(word)
print(f'You typed in {len(lst)} different words')