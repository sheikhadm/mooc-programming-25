# Write your solution here
def new_person(name:str,age:int):
    bn = name.split(' ')
    if name == ' ' or len(name) > 40 or age < 0 or age > 150 or len(bn) < 2 :
        raise ValueError('Invalid Parameter')
    return (name,age)

if __name__ == "__main__":
    new_person('James Jameson', 32)
