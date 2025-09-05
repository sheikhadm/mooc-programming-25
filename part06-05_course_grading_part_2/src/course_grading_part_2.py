# write your solution here
# write your solution here
# student information = si
# exercises completed = ec
si = input('Student information: ')
ec = input('exercises completed: ')
ep = input('Exam points: ')


students = {}

with open(si) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        students[parts[0]] = f'{parts[1]} {parts[2]}'.strip()

exercises = {}

with open(ec) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] != 'id':
            exercises[parts[0]] = []
            for x in parts[1:]:
                exercises[parts[0]].append(int(x))

points= {}

with open(ep) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] != 'id':
            points[parts[0]] = []
            for x in parts[1:]:
                points[parts[0]].append(int(x))

                
for pic, name in students.items():
    cn = 0
    if pic in points:
        e = (sum(exercises[pic]) / 40) * 10
        ex = int(e) + sum(points[pic])
        if ex > 0 and ex < 15:
            cn = 0
        elif ex > 14 and ex < 18:
            cn = 1
        
        elif ex  > 17 and ex < 21:
            cn =2
        
        elif ex > 20 and ex < 24:
            cn = 3
        
        elif ex > 23 and ex < 28:
            cn = 4
        
        elif ex > 27 :
            cn = 5
        
        print(f"{name} {cn}")
    else:
        print(f"{name:16} 0 euros")


