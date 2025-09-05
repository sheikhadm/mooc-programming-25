# Write your solution here
def line (x,word) :
    if word == '':
        print('*' * x)
    else:
        print (word[0] * x)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x0")