# To add two numbers
def dual_add(x,y) :
    sum = x + y
    print(sum)

# To add three numbers
def tri_add(x,y,z) :
    sum = x + y + z
    print(sum)

# To sub two numbers
def sub(x,y) :
    sub = x - y
    print(sub)
dual_add(10,20)
tri_add(10,20,30)
sub(10,20)

# Returning value from function
def add(a,b):
    sum = a + b
    return sum
print(add(20,30))

#This function find large number between two numbers
def large(a,b):
    if a>b:
        return a
    else:
        return b
print(large(30,60))


