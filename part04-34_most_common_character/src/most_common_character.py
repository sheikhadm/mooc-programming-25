# Write your solution here
def most_common_character( word):
    mst = 0
    n = ''
    for x in word:
        c = word.count(x)
        if c > mst:
            mst = c
            n = x
    return n

if __name__ == "__main__":
    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
        

     