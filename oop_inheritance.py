#  Inheritance
# Enables a class (child) to inherit attributes and methods from another class (parent).
# Promotes code reuse.

# Syntax: 

class Parent:
    pass

class Child(Parent):  # Child inherits Parent
    pass

# Sample code 
class Vehicle:
    def description(self):
        return "This is a vehicle"

class Car(Vehicle):
    def description(self):
        return "This is a car"

car = Car()
print(car.description())  # Output: This is a car

