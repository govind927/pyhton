#understanding conditional statements

# age = float(input("Enter your age here -> "))

# if(age > 18):
#     print("Yes , your are eligible for Vote")

# if(age > 60):
#     print("You are an senior citizen!!!")

# elif(age == 18):
#     print("You are still eligible for Vote")

# elif(age <= 0):
#     print("Enter Valid age!!!")

# else:
#     print("You are not eligible for Voting!!!")

#Program to get greatest of Four numbers enter by user

# num1 = int(input("Enter number here -> "))
# num2 = int(input("Enter number here -> "))
# num3 = int(input("Enter number here -> "))
# num4 = int(input("Enter number here -> "))

# if(num1 > num2 and num1 > num3 and num1 > num4):
#     print("Num1 is greatest")
# elif(num2 > num1 and num2 > num3 and num2 > num4):
#     print("Num2 is greatest")
# elif(num3 > num1 and num3 > num2 and num3 > num4):
#     print("Num3 is greatest")
# else:
#     print("Num4 is greatest")



#Program to check if a student is passed or not
#overall marks > 33  and each subject > 40 and total 3 subjects


sub1 = float(input("Enter sub1 marks here -> "))
sub2 = float(input("Enter sub2 marks here -> "))
sub3 = float(input("Enter sub3 marks here -> "))

marks = sub1 + sub2 + sub3 
percentage = (marks / 300) * 100

if(sub1 >=33 and sub2 >=33 and sub3 >= 33 and percentage > 40):
    print("Passed!!!" , percentage)

else:
    print("You Failed! try again next Year" , percentage)
