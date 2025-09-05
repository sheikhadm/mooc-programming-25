# Write your solution here
def fact(n: int):
    c= 1
    for x in range(1,n + 1):
        c *= x
    return c

def factorials(n : int):
    bic = {}
    for x in range(1,n + 1):
        cn = fact(x)
        bic[x] = cn
    return bic

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
