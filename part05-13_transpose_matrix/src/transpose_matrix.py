# Write your solution here

def transpose(matrix : list):
    i = 1
    j = 0
    c= []
    while j < len(matrix):
        while i < len(matrix):
            ns = str(j) +str(i)
            ps = str(i) + str(j)
            c.append(ns)
            if ps in c:
                pass
            else:
                a = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = a
            i += 1
        j+=1
        i = 1

if __name__ == "__main__":
    matix = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
    transpose(matix)
    print(matix)
    