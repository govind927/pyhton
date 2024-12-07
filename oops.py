#creating class student
class Student: 
    college_Name = "XYZ"  #this is a class attribute
    # def __ininit__ (self): # initialize a constructor with self paramater
    #     pass

    # Creatin a parameterised constructor
    def __init__(self , name , marks): 
        
        # Assigning attributes to instances / objects
        self.name = name 
        self.marks = marks
        print("Adding students in Database : ")

    # Creating a simple python Method
    def welcome(self):               
        print("Welcome Student" , self.name)

    def getMarks(self):
        print(self.marks)
    
s1 = Student("Rahul" , 83)
print(s1.name , s1.marks)

s1.welcome()
s1.getMarks()
        
    

