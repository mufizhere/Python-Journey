# 1. INHERITANCE
# - Inheritance allows a class to reuse or extend another class.
# - The existing class is called the parent class.
# - The new class is called the child class.

class Car:

    def start(self):
        print("Car engine started.")


class ElectricCar(Car):

    def charge(self):
        print("Electric car is charging.")


car = ElectricCar()

car.start()
car.charge()

# Output:
# Car engine started.
# Electric car is charging.