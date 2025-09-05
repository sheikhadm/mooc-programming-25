# Write your solution here
def read(fn:str):
    with open(fn) as new_file:
        for line in new_file:
            print(line.strip())

while True:
    fn = 'diary.txt'
    print('1 - add an entry, 2 - read entries, 0 - quit')
    fnc = input('Function: ')
    if fnc == '1':
        entry = input('Diary entry: ')
        with open(fn , 'a') as new_file:
            new_file.write(f'{entry}\n')
    elif fnc == '2':
        read(fn)
    elif fnc == '0':
        print('Bye now!')
        break

