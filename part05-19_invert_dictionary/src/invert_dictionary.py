# Write your solution here
def invert(dictionary: dict):
    c = {}
    for k , v in dictionary.items():
        if k in dictionary:
            c[v] = k
    dictionary.clear()
    dictionary.update(c)
            

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)