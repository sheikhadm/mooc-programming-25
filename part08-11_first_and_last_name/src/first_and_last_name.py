# Write your solution here:
class Person():
    def __init__(self,name):
        self.name = name

    def return_first_name(self):
        f = self.name.split(' ')
        return f[0]
    
    def return_last_name(self):
        f = self.name.split(' ')
        return f[1]

if __name__ == "__main__":
    peter = Person("Peter Pythons")
    print(peter.return_first_name())
    print(peter.return_last_name())













