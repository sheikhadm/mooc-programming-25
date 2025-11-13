# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string,forbidden):
    return "".join([num for num in string if num not in forbidden])

if __name__ == "__main__":
    sentence = "Once! upon, a time: there was a python!??!?!"
    filtered = filter_forbidden(sentence, "!?:,.")
    print(filtered)
