# Write your solution here
import json
def print_persons(fn:str):
    with open(fn) as new_file:
        data = new_file.read()
    students = json.loads(data)
    for x in students:
        print(f'{x['name']} {x['age']} years ({', '.join(x['hobbies'])})')

if __name__ == "__main__":
    print_persons('file1.json')
