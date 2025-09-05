# write your solution here

def largest():
    large = 0
    with open('numbers.txt') as new_file:
        for line in new_file:
            if int(line) > large: 
                large = int(line)
        return large
        

if __name__ == "__main__":
    print(largest())