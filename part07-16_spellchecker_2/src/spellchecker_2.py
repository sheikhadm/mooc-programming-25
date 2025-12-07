# Write your solution here
wt = input('Write text: ')

words = []

with open('wordlist.txt') as new_file:
    for line in new_file:
        words.append(line.strip())

parts = wt.split(' ')
c = []
for x in parts:
    if x.lower() not in words:
        x = '*' + x + '*'
    c.append(x)
sentence = " ".join(c)
print(sentence)
