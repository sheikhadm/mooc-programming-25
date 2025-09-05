# Copy here code of line function from previous exercise and use it in your solution
def line (x,word) :
    if word == '':
        print('*' * x)
    else:
        print (word[0] * x)

def pnt (x,y,word):
    i = 0
    while i < y:
       line(x, word)
       i += 1
def triangle(size,word):
    # You should call function line here with proper parameters
    i = 1
    while i <= size:
       line(i, word)
       i += 1


def shape(x,word1 , y ,word2):
    triangle(x,word1)
    pnt(x,y,word2)
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")