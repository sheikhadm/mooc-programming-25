# Write your solution here
while True: 
    word = input('Editor: ')
    if 'visual studio code' == word.lower():
        print("an excellent choice!")
        break
    elif 'notepad' == word.lower() or 'word' == word.lower():
        print('awful')
    else:
        print('not good')
