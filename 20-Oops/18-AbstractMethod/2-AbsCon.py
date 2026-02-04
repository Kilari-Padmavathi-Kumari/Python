from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print(self.brand, "car starts with key")

class Bike(Vehicle):
    def start(self):
        print(self.brand, "bike starts with kick")

c = Car("Toyota")
b = Bike("Honda")

c.start()
b.start()
