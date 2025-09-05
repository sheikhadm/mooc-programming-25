# Write your solution here
book = {}
while True :
    cmd = int(input('command (1 search, 2 add, 3 quit): '))
    if cmd == 3 :
        print('quitting...')
        break
    elif cmd == 2:
        name = input('name: ')
        number = input('number: ')
        if name not in book:
            book[name] = []
        book[name].append(number)
        print('ok!')
    elif cmd == 1:
        name = input('name: ')
        if name not in book:
            print ('no number')
        else:
            for k in book[name]:
                print(k)