"""
lambda function is called unnamed or anonymous function.
It is used for one line short expression/code.
"""
#In general function
"""def calculate(a,b):
    sum = a * a + 2 * a * b + b * b
    print(sum)"""

#In lambda function
print((lambda a, b: a*a + 2*a*b + b*b)(2, 3))

#it might be done as
calculate = (lambda a, b: a*a + 2*a*b + b*b)(8, 6)
print(calculate)