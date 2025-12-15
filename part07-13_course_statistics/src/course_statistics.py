# Write your solution here
import urllib.request
import json
import math
def retrieve_all():
    course_list = []
    my_request = urllib.request.urlopen(" https://studies.cs.helsinki.fi/stats-mock/api/courses")
    courses = json.loads(my_request.read())
    for x in courses:
        if x['enabled'] == True:
            course_list.append((x['fullName'],x['name'],x['year'],sum(x['exercises'])))
    return (course_list)

def retrieve_course(course_name:str):
    course_info = {}
    hours = 0
    exercises = 0
    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"

    my_request = urllib.request.urlopen(url)
    course = json.loads(my_request.read())
    for k,v in course.items():
        hours += int(v['hour_total'])
        exercises += v['exercise_total'] 
    students = max(course.items(), key = lambda item:item[1]['students'])
    students = students[1]['students']
    return {
        'weeks' :len(course),
        'students' : students ,
        'hours': hours ,
        'hours_average':math.floor(hours/ students),
        'exercises' : exercises,
        'exercises_average' : math.floor(exercises/students) 
         
    }


if __name__ == "__main__":
    print(retrieve_course('docker2019'))
    