"""
Recursion means the repeating/returning of a function.
"""
def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))