# write your solution here
# student information = si
# exercises completed = ec
si = input('Student information: ')
ec = input('exercises completed: ')


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
                
for pic, name in students.items():
    if pic in exercises:
        exercise = sum(exercises[pic])
        print(f"{name} {exercise}")
    else:
        print(f"{name:16} 0 euros")



