# 2. ENCAPSULATION
# - Encapsulation combines data and methods inside a class.
# - It can provide controlled access to object data.
# - A double underscore triggers name mangling in Python.


class Car:

    def __init__(self, speed):
        self.__speed = speed

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        if speed >= 0:
            self.__speed = speed
        else:
            print("Speed cannot be negative.")


car = Car(60)

print(car.get_speed())
car.set_speed(100)

print(car.get_speed())
car.set_speed(-20)

# Output:
# 60
# 100
# Speed cannot be negative.