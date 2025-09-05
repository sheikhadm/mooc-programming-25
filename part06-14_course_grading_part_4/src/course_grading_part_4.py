# tee ratkaisu tänne
# write your solution here
# write your solution here
# student information = si
# exercises completed = ec
si = input('Student information: ')
ec = input('exercises completed: ')
ep = input('Exam points: ')
ci = input('Course information: ')


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

course = {}

with open(ci) as new_file:
    for line in new_file:
        line = line.strip()
        parts = line.split(':')
        course[parts[0]] = parts[1]

with open('results.txt', 'w') as new_file:
    new_file.write(f'{course['name'].lstrip()},{course['study credits']} credits \n')
    new_file.write(f'{'=' * 38}\n')
    new_file.write(f'{'name':30}{'exec_nbr':10}{'exec_pts.' :10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n')
with open('results.csv','w') as new_file:
    pass
for pic, name in students.items():
    cn = 0
    if pic in points:
        exec_c = int(sum(exercises[pic]))
        exec_p = int(sum(points[pic]))
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
        with open('results.txt', 'a') as new_file:
            new_file.write(f'{name:30}{exec_c:<9}{int(e) :< 10}{exec_p: < 10}{ex:< 11}{cn:<10} \n')
        with open('results.csv','a') as new_file:
            new_file.write(f'{pic};{name};{cn}\n')
    else:
        print(f"{name:16} 0 euros")





