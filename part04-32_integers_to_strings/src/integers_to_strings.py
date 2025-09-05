# Write your solution here
def formatted (lst):
    ln = []
    for x in lst:
        c = round(x,2)
        ln.append(f'{c:.2f}')
    return ln

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)
