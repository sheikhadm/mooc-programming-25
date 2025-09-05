# Write your solution here
def spruce(x):
    print('a spruce!')
    num = (x * 2) - 1
    num = num // 2
    end = num
    i = 1
    y = 0
    while y < x :
        print(f'{' '* num}{'*' * i}')
        num -= 1
        i += 2
        y += 1
    print(f'{' ' * end}*')

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)