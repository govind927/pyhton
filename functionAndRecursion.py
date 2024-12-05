#Function definition :
# def my_fun():
#     print("Hello Sir!!!")

#function call
# my_fun()

#Function with arguments
# def fact(num):
#     fact = 1
#     for i in range(1 , num + 1):
#         fact = fact * i
#     print(f"Factorial of {num} is {fact}")
#     return fact
# fact(0)

#Factorial of number by Recursion
# def factorial(n):
#     if(n == 0 or n == 1):
#         return 1
#     return n * factorial(n - 1)

# n = int(input("N = "))
# print(f"The factorial of this number is {factorial(n)}")

# Function to find greatest of three numbers

# def greatest():
#     n1 = int(input("Enter n1 : "))
#     n2 = int(input("Enter n2 : "))
#     n3 = int(input("Enter n3 : "))

#     if(n1 > n2 and n1 > n3):
#         print("n1 is greatest")
#     if(n2 > n1 and n2 > n3):
#         print("n2 is greatest")
#     if(n3 > n2 and n3 > n1):
#         print("n3 is greatest")
#     else:
#         print("Enter distinct Numers")

# greatest()

# Function to create Celsius to Fahrenheit
# def celToFah():
#     tempInCel= float(input("Enter temp in cel -> "))
#     tempInFah = ((9 / 5) * tempInCel) + 32

#     return tempInFah
# print(f"This temp in Fahrenheit will be {celToFah()}")

