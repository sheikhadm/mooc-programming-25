# Write your solution here
def first_word (sentence):
    num = sentence.find(' ')
    return sentence[:num]

def second_word (sentence):
    num = sentence.find(' ')
    n = num + 1
    new_sentence = sentence[n:]
    if new_sentence.find(' ') != -1:
       num = new_sentence.find(' ')
       nm = num
       return new_sentence[:nm]
    else:
        return new_sentence

def last_word (sentence):
    num = len(sentence)
    i = num - 1
    while i >= 0:
        if sentence[i] == ' ':
            i += 1
            return sentence[i:]
        i -= 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "happily ever after"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))