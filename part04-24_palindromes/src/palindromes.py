# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
def palindromes(word:str):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else : return False

def main():
    while True:
        word = input('Please type in a palindrome: ')
        if palindromes(word):
            print(f'{word} is a palindrome!')
            break
        else:print('that wasn\'t a palindrome')

main()
