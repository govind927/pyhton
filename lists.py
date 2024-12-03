#Understand Python Lists here
l = [0 , 1.1 , -5 , "Rahul" , [2 , 5 , 8] , "Govind" , "108"]
print("Original List : " , l)

l.append(7)
print(l)

l.insert(2 , "pi")
print(l)

# l.sort()
# print(l)

l.reverse()
print(l)

print(l.pop(0))
print(l)

l.remove(-5)
print(l)

l.index("108")
print(l)

print(l[1 : 4])

