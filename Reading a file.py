file = open("file.txt", "r")
#print(file.readable())
text = file.readlines()
print(text)


#using for loop
for line in file:
    print(line)

file.close()