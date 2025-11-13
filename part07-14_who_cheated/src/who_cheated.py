# Write your solution here
import csv
from datetime import datetime, timedelta

def cheaters():
    students = {}
    cheats = []
    with open('start_times.csv') as new_file:
        for line in csv.reader(new_file , delimiter = ';'):
            ftime = datetime.strptime(line[1],"%H:%M")
            finish_time = ftime + timedelta(hours=3)
            students[line[0]] = (line[1],finish_time)

    with open('submissions.csv') as new_file:
        for line in csv.reader(new_file, delimiter = ';'):
            if line[0] in students:
                stime = datetime.strptime(line[3], "%H:%M")
                if stime > students[line[0]][1]:
                    if line[0] in cheats:
                        continue
                    else:
                        cheats.append(line[0])
    return cheats


if __name__ == '__main__':
    cheaters() 