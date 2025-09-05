# write your solution here
def read_fruits():
    with open('fruits.csv') as new_file:
        cn = {}
        for line in new_file:
            line = line.replace('\n', '')
            parts = line.split(';')
            name = parts[0]
            vn = parts[1]
            cn[name] = float(vn)
        return cn

if __name__ == "__main__":
   print( read_fruits())
