# Write your solution here
lst = [1,2,3,4,5]
while True :
    ind = int(input('Index: '))
    if ind == -1:
        break
    new = int(input('New value: '))
    lst[ind] = new
    print(lst)