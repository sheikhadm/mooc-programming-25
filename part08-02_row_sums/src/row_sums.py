# Write your solution here
def row_sums(m:list):
    for x in m:
        c = sum(x)
        x.append(c)

if __name__ =="__main__":
    my_matrix = [[1, 1], [2, 2]]
    row_sums(my_matrix)
    print(my_matrix)
