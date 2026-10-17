# 3. POLYMORPHISM
# - Different classes can implement the same method differently.
# - The same method call can produce different behavior.

class PetrolCar:

    def start(self):
        print("Petrol engine started.")


class ElectricCar:

    def start(self):
        print("Electric motor started.")


cars = [PetrolCar(), ElectricCar()]

for car in cars:
    car.start()
    
# Output:
# Petrol engine started.
# Electric motor started.