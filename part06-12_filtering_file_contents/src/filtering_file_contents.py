# Write your solution here
def check(tup):
    np = eval(tup[1])
    if int(tup[2]) == np:
        return True
    else:
        return False
def filter_solutions():
    mts = {}
    with open('solutions.csv') as new_file:
        i = 0
        for line in new_file:
            line.strip()
            parts = line.split(';')
            i +=1
            mts[i] = (parts[0],parts[1], parts[2])
        with open("correct.csv", "w") as my_file:
            pass
        with open("incorrect.csv", "w") as my_file:
            pass
        for k,v in mts.items():
            if check(v):
                with open('correct.csv','a') as new_file:
                    new_file.write(f'{v[0]};{v[1]};{v[2]}')
            elif not check(v):
                with open('incorrect.csv','a') as new_file:
                    new_file.write(f'{v[0]};{v[1]};{v[2]}')

if __name__ == "__main__":
    filter_solutions()

            

