# Write your solution here
def find_words(st:str):
    lst = []
    words = []
    low =st.lower()
    with open('words.txt') as new_file:
        for line in new_file:
            line = line.strip()
            words.append(line)

    for x in words:
        p = True
        if '.' in low:
            if len(x) != len(low):  
                continue
            for i in range(len(low)):
                if i >= len(x) or (x[i] != low[i] and low[i] != '.'):
                    p = False
                    break
            if p == True:
                lst.append(x)
        elif '*' in low:
            if low[-1] == '*' and x.startswith(low[:-1]):
                lst.append(x)
            elif low[0] =='*' and x.endswith(low[1:]):
                lst.append(x)
        elif x == low:
            lst.append(x)
    return lst

if __name__ == "__main__":
    print(find_words("p.ng"))


            