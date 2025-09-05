# Write your solution here
def add_student(dic : dict , name: str):
    if name not in dic:
        dic[name] = {
            'tuples':[],
            'courses':0,
            'avg': 0
        }



def print_student(dic:dict, name: str):
    sm = 0
    if name in dic:
        print(f"{name}: ")
        if dic[name]['tuples'] == []:
            print(' no completed courses')
        else:
            print(f" {len(dic[name]['tuples'])} completed courses:")
            dic[name]['courses'] = len(dic[name]['tuples'])
            for x in dic[name]['tuples']:
                print(f"  {x[0]} {x[1]}")
                sm += x[1]
            dic[name]['avg'] = sm/len(dic[name]['tuples'])
            print(f' average grade {dic[name]['avg']}')
    else:print(f'{name}: no such person in the database')

def action(dic:dict, name: str):
    sm = 0
    if name in dic:
            dic[name]['courses'] = len(dic[name]['tuples'])
            for x in dic[name]['tuples']:
                sm += x[1]
            dic[name]['avg'] = sm/len(dic[name]['tuples'])
    



def check_course(dic, course,name):
    for i, x in enumerate(dic[name]['tuples']):
        if course[0] == x[0] and course[1] < x[1]:
            return False
        elif course[0] == x[0] and course[1] > x[1]:
            temp = list(x)
            temp[1] = course[1]
            dic[name]['tuples'][i] = tuple(temp)
            return "updated"
        
    return True

def add_course(dic: dict, name: str, course: tuple):
    if name in dic:
        if course[1] > 0:
            result = check_course(dic, course, name)
            if result is True:
                dic[name]['tuples'].append(course)
                action(dic, name)
            elif result == 'updated':
                action(dic, name)  # Update the average after changing grade
    else:
        print(f'{name}: no such person in the database')


def summary(dic):
    print(f"students {len(dic)}")
    most = 0
    most_name = ''
    best = 0
    best_name = ''
    for k,v in dic.items():
        if most < v['courses']:
            most = v['courses']
            most_name = k
        if best  < v['avg']:
            best = v['avg']
            best_name = k
    print(f'most courses completed {most} {most_name}')
    print(f'best average grade {best} {best_name}')




            

if __name__ == "__main__":
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    print_student(students, "Emily")
    print_student(students, "Peter")

# add_student(students, "Emily")
# add_student(students, "Peter")
# add_course(students, "Emily", ("Software Development Methods", 4))
# add_course(students, "Emily", ("Software Development Methods", 5))
# add_course(students, "Peter", ("Data Structures and Algorithms", 3))
# add_course(students, "Peter", ("Models of Computation", 0))
# add_course(students, "Peter", ("Data Structures and Algorithms", 2))
# add_course(students, "Peter", ("Introduction to Computer Science", 1))
# print_student(students, "Emily")
# print_student(students, "Peter")

# add_student(students, "Emily")
# add_student(students, "Peter")
# add_course(students, "Emily", ("Software Development Methods", 4))
# add_course(students, "Emily", ("Software Development Methods", 5))
# add_course(students, "Peter", ("Data Structures and Algorithms", 3))
# add_course(students, "Peter", ("Models of Computation", 0))
# add_course(students, "Peter", ("Data Structures and Algorithms", 2))
# add_course(students, "Peter", ("Introduction to Computer Science", 1))
# add_course(students, "Peter", ("Software Engineering", 3))
# summary(students)
# summary(students)
        