# Write your solution here
def histogram(string : str):
    b = {}
    for x in string:
        if x not in b:
            b[x] = 0
        b[x] += 1
    for k,v in b.items():
        print(f'{k} {"*" * v}')

if __name__ == "__main__":
    histogram("abba")
    histogram("statistically")
