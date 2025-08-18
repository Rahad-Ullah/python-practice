"""
formate of comprehension list:
[expression for item in list]
Note: In comprehension list you must use [] "square bracket"
"""
#In 'map function' and list
num = [1,2,3,4,5]
result = list(map(lambda x: x*x, num))
print(result)

#After using "comprehension list"
result = [x*x for x in num]
print(result)

"""Example -2"""
#Before using "comprehension list"
result = list(filter(lambda x: x%2==0, num))
print(result)

#After using "comprehension list"
result = [x for x in num if x%2==0]
print(result)
