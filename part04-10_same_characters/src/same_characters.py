# Write your solution here
def same_chars(word,x,y):
    if word[x] == word[y]:
        return True
    else:
        return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    result = same_chars("coder", 1, 2)
    print(result)