# Write your solution here
def list_sum(a,b):
    i = 0
    lst = []
    while i < len(a):
        nw = a[i] + b[i]
        lst.append(nw)
        i += 1
    return lst

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))
