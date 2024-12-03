#Understand Python Tuples
t = (1 , 2.0 , "Three" , True , "Govind" , 1 , (2 , 4 , 6))
u = (1 , 3 , 5 , 7)

print(type(t))

print(t.count(1))

print(t.index(True))

print(t[1])

print(t+u)

print(t * 2)

print(2.0 in t)

for item in t:
    print(item)  # iteration in tuples

print(len(t))

print("Max in tuple U : " , max(u))
print("Min in tuple U : " , min(u))

print("Sum of elements in u: " , sum(u))

print("Sorted Tuple : " , sorted(u))

print(t[6])




