# Polymorphism
# Allows methods to have the same name but behave differently based on the object.
# Achieved via:
# Method Overriding (in subclasses).
# Method Overloading (not directly supported, but can be simulated).

#Sample program

class Bird:
    def fly(self):
        return "Flying!"

class Penguin(Bird):
    def fly(self):
        return "Cannot fly!"

bird = Bird()
penguin = Penguin()

print(bird.fly())  
print(penguin.fly())  
