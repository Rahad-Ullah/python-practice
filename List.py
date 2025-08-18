"""
format of list:
variable = [something, something, something, something, something]
Note: You must be use [] "square bracket" in list.
"""

subject = ["C", "C++", "Java", "Python", "JavaScript", "NodeJS"]
print(subject)
print(subject[2])
print(subject[2:])
print(subject[2:5])
print(subject[-3])

#function realated to list
#1. To add something
subject.append("Django")
print(subject)
#2. Insert function
subject.insert(2,"BOOTSTRAP")
print(subject)
#3. Remove function
subject.remove("Java")
print(subject)
#sorting
subject.sort()
print(subject)
#reverse sorting
subject.reverse()
print(subject)
#pop sorting
subject.pop()
subject.pop()
print(subject )
