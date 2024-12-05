#Understanding While  , For and Do - While loops

#Problem 1 -> Print numbers from 1 to n 

# # using while loop
# i = 1
# n = int(input("Enter your number : "))
# while (i <= n):
#     print(i)
#     i += 1

# print("End of Program")


#Using for loop
# for i in range(0 , n , 2):
#     print(i)

# print("End of Program")

# PROBLRM 2 -> Iterate List elements using for Loop
# l = [1 , 2 , 3 , 4 , 5]
# i = 0

# for i in l:
#     print(i)
#     i = i + 1
#     # i < len(l)
    

# print("End of Program")

# This is a sample string
# s = "This is a sample string"
# for i in s:
#     print(i)

# PROBLEM 3 -> Program to print table of a given number

# n = int(input("Enter number : "))
# for i in range(1 , 11):
#     print(n ,"*",i ," = " , n * i)


# PROBLEM 4 -> Program to check if number is prime or not

# n = int(input("Enter number : "))
# for i in range(2 , n):
#     if((n % i) == 0):
#         print(n , " is not a Prime Number")
#         break
    
#     else:
#         print(n , " is a Prime Number")
#         break

# print("End of Program")

# PROBLEM 5 -> Program to check if number is prime or not IMPROVED VERSION USING GPT
#LOGIC : IF N DIVIDES BY ANY NUMBER UPTO SQRT OF N -> IT IS NOT A PRIME NUMBER
# import math

# n = int(input("Enter number: "))

# if n <= 1:
#     print(n, "is not a Prime Number")
# else:
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if (n % i) == 0:
#             print(n, "is not a Prime Number")
#             break
#     else:
#         print(n, "is a Prime Number")

# print("End of Program")


# PROBLEM 6 -> Program to find sum of first N natural numbers
#Formula = n(n + 1) // 2 for efficient code

# n = int(input("Enter Number: "))
# total = 0 
# for i in range(1 , n+1):
#     total += i
# print(f"Sum of first {n} numbers is = {total}")
# print("End of Program")


# PROBLEM 7 -> Program to find Factorial of a number
# n = int(input("Enter number to check Factorial : "))
# fact = 1
# for i in range(1 , n + 1):
#     fact = fact * i
# print(f"The factorial of {n} is {fact}")


# PROBLEM 8 -> Pattern Printing
'''
***
* *   Program to print this Pattern for N = 3
***
'''
# Program to print the pattern for N using a for loop
# N = int(input("Enter number : "))

# # Loop to print the pattern
# for i in range(N):
#     if i == 0 or i == N - 1:
#         # Print the first and last rows with N stars
#         print('*' * N)
#     else:
#         # Print the middle rows with 1 star, then spaces, then 1 star
#         print('*' + ' ' * (N - 2) + '*')


# PROBLEM 9 -> Table in reverse oreder using for Loop
n = int(input("Enter number : "))
for i in range(1, 11):
    print(n , "*" , (11 - i) , " = " , n * (11 - i))
    








