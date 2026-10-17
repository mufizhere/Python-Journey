# 4. ABSTRACTION
# - Abstraction defines required behavior.
# - Concrete subclasses provide the implementation.
# - Python supports abstraction through the abc module.

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class PetrolCar(Vehicle):

    def start(self):
        print("Starting the petrol engine.")


class ElectricCar(Vehicle):

    def start(self):
        print("Starting the electric motor.")


car1 = PetrolCar()
car2 = ElectricCar()

car1.start()
car2.start()

# Output:
# Starting the petrol engine.
# Starting the electric motor.