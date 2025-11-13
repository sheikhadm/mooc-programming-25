# tee ratkaisusi tänne
class Course():
    def __init__(self, name:str , grade:int, credit:int):
        self.__name = name
        self.__grade = grade
        self.__credit = credit
    
    def __str__(self):
        return f'{self.__name} ({self.__credit} cr) grade {self.__grade}'
    
    @property
    def grade(self):
        return self.__grade
    
    @property
    def credit(self):
        return self.__credit

class Record:
    def __init__(self):
        self.__records = {}

    def help(self):
        print("1 add course")
        print("2 get course data")
        print('3 add statistics')
        print("0 exit")
       
        

    def add_course(self):
        name = input("course: ")
        grade = input("grade: ")
        credit = input("credits: ")
        if not name in self.__records:
            self.__records[name] = Course(name,grade,credit)
        else:
            if grade > self.__records[name].grade:
                self.__records[name] = Course(name,grade, credit)
            
    
    def distribution(self):
        credit = 0
        grade = 0
        grades= {5:0,4:0,3:0,2:0,1:0}
        for k,v in self.__records.items():
            credit += int(v.credit)
            grade += int(v.grade)
            if not int(v.grade) in grades:
                grades[int(v.grade)]= 1
            else:
                grades[int(v.grade)] += 1
        print(f'{len(self.__records)} completed courses, a total of {credit} credits')
        print(f'mean {grade / 5}')
        print(f'grade distribution')
        print(f'5: {'x' * grades[5]}')
        print(f'4: {'x' * grades[4]}')
        print(f'3: {'x' * grades[3]}')
        print(f'2: {'x' * grades[2]}')
        print(f'1: {'x' * grades[1]}')

    def search(self):
        name = input("name: ")
        if not name in self.__records:
            print('no entry for this course')
        else:
            print(self.__records[name])
        
     

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.search()
            elif command == '3':
                self.distribution()
            else:
                self.help()


application = Record()
application.execute()