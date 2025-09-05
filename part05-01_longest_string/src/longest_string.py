# Write your solution here
def longest(lst :list):
    lng = 0
    s = ''
    for x in lst:
        if len(x) >= lng :
            lng = len(x)
            s = x
            for c in x:
                if c == ' ':
                    lng -= 1
    return s

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))





            
