# Write your solution here
def read_input(st :str,x :int,y : int):
    while True:
        try:    
            nm = int(input(f'{st}'))
            if nm > x and nm < y:
                return nm
        except ValueError:
            pass
        print(f'You must type in an integer between {x} and {y}')

if __name__ == "__main__" :
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)