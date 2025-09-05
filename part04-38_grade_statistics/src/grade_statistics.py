# Write your solution here
lst = []
gz = 0
go = 0
gt = 0
gtr = 0
gf = 0
gfi = 0
i = 0
while True:
    num = input('Exam points and exercises completed: ')
    
    if num == "":
        break
    cn = num.split(" ")
    ep = (int(cn[1]) / 100) * 10
    bth = ep + int(cn[0])
    lst.append(int(bth))
    if int(cn[0]) < 10 or bth <= 14:
        gz += 1
    elif bth > 14 and bth < 18:
        go += 1 
        i +=1
    elif bth > 17 and bth < 21:
        gt += 1 
        i += 1
    elif bth > 20 and bth < 24:
        gtr += 1 
        i += 1
    elif bth > 23 and bth < 28:
        gf += 1 
        i += 1
    elif bth > 27 and bth < 31:
        gfi += 1 
        i += 1
pp = (i / len(lst)) * 100
total = sum(lst)
pa = total / len(lst)

print('Statistics: ')
print(f'Points average: {pa}')
print(f'Pass percentage: {round(pp, 1)}')
print('Grade distribution: ')
print(f'  5: {'*' * gfi}')
print(f'  4: {'*' * gf}')
print(f'  3: {'*' * gtr}')
print(f'  2: {'*' * gt}')
print(f'  1: {'*' * go}')
print(f'  0: {'*' * gz}')
