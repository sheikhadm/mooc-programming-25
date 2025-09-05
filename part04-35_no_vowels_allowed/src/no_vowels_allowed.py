# Write your solution here
def no_vowels(word):
    lst = []
    for x in word:
        if x  != 'a' and x != 'e' and x != 'i' and x != 'o' and x != 'u':
             lst.append(x)
    return ''.join(lst)

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))


