# Write your solution here
import csv
from datetime import datetime, timedelta

def cheaters():
    students = {}
    task = {}
    with open('start_times.csv') as new_file:
        for line in csv.reader(new_file , delimiter = ';'):
            ftime = datetime.strptime(line[1],"%H:%M")
            finish_time = ftime + timedelta(hours=3)
            students[line[0]] = (line[1],finish_time)

    with open('submissions.csv') as new_file:
        for line in csv.reader(new_file, delimiter = ';'):
            if line[0] in students:
                stime = datetime.strptime(line[3], "%H:%M")
                if stime < students[line[0]][1]:
                    if line[0] not in task:
                       task[line[0]]={}
                       task[line[0]][line[1]]= line[2]
                    elif line[0] in task:
                        if line[1] in task[line[0]]:
                            if line[2]> task[line[0]][line[1]]:
                                task[line[0]][line[1]] = line[2]
                        else:
                            task[line[0]][line[1]]= line[2]
    return task


                    

def final_points():
    data = cheaters()
    correct = {}
    total = 0
    for k,v in data.items():
        name = k
        total = 0
        for k,v in v.items():
            total = total + int(v)
            
        correct[name] =total
    return correct


if __name__ == "__main__":
    print(final_points())
    