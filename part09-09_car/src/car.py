# WRITE YOUR SOLUTION HERE:

class Car:
    def __init__(self):
        self.__pet = 0
        self.__odo = 0

    def __str__(self):
        return f'Car: odometer reading {self.__odo} km, petrol remaining {self.__pet} litres'

    def fill_up(self):
        self.__pet = 60
    
    def drive(self,km:int):
        self.__odo = km
        if km >= self.__pet:
            self.__pet = 0
        else:
            self.__pet -= km

if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)