

def balanced_brackets(my_string: str):
    allowed_list = ['(',')','[',']']
    my_string = ''.join([x for x in my_string if x  in allowed_list])
    if len(my_string) == 0:
        return True
    
    if not (my_string[0] == '(' and my_string[-1] == ')' or my_string[0] == '[' and my_string[-1] == ']'):
        return False

    # remove first and last character
    return balanced_brackets(my_string[1:-1])

if __name__ == "__main__":
    

    ok = balanced_brackets("(x + 1)(y + 1)")
    print(ok)