# Write your solution here
import random

def words( n : int ,begin : str):
    wds = []
    with open('words.txt') as new_file:
        for line in new_file:
            line = line.strip()
            if line.startswith(begin):
                wds.append(line)
        random.shuffle(wds)
        if len(wds) < n:
            raise ValueError ('invalid parameter')
        elif len(wds) > n:
            d = n
            c = wds[:d]
            return c
        return wds

if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)