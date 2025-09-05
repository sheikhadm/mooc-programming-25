# Write your solution here
def store_personal_data(person:tuple):
    name = person[0]
    age = int(person[1])
    height = float(person[2])
    with open('people.csv','a') as new_file:
        new_file.write(f'{name};{age};{height}\n')

if __name__ == "__main":
    store_personal_data("Paul Paulson", 37, 175.5)

