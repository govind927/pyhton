# f = open("notes.txt")
# data = f.readline()
# print(data)
# print(type(data))
# f.close()
# refer notes for more details

with open("notes.txt") as f:
    print(f.readline())
    # ny using with function we don't need to close file explicitely
    