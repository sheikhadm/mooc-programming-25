# Write your solution 
#o = orig_string
def change_case(o:str):
    nw = []
    for x in o:
        if x.islower():
            nw.append(x.upper())
        elif x.isupper():
            nw.append(x.lower())
        else:
            nw.append(x)
    final = ''.join(nw)
    return final

def split_in_half(o:str):
    hf = len(o)//2
    return (o[:hf],o[hf:])

def remove_special_characters(orig_string: str):
    chars = []  
    
    for char in orig_string:
        if char.isalnum() or char == " ":
            chars.append(char)
    
    return ''.join(chars)

if __name__ == "__main__":
    my_string = "Well hello there!"
    print(change_case(my_string))

    p1, p2 = split_in_half(my_string)
    print(p1)
    print(p2)

    m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)
        