# Write your solution here
import csv
from datetime import datetime, timedelta

def cheaters():
    students = {}
    with open('start_times.csv') as new_file:
        for line in csv.reader(new_file , delimiter = ';'):
            ftime = datetime.strptime
            student[line[0]] = line[1]
    
    with open('submissions.csv') as new_file:
        for line in 