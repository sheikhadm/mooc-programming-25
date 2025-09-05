# Write your solution here
import string
def separate_characters(my_string: str):
    letter = string.ascii_letters
    letters = ''
    punc = ''
    white = ''
    for x in my_string:
        if x in letter:
            letters += x
        elif x in string.punctuation:
            punc += x
        else:
            white += x
    return((letters,punc,white))

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts)
    # print(parts[0])
    # print(parts[1])
    # print(parts[2])