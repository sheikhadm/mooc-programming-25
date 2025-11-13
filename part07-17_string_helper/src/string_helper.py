# Write your solution 
#o = orig_string
def change_case(o:str):
    nw = []
    for x in o:
        if x.islower():
            nw.append(x.upper())
        elif x.isupper():
            nw.append(x.lower())
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
        