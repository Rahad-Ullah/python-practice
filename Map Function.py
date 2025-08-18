def square(x):
    return x*x

num = [1,2,3,4,5,6]

#In "map function" another funtion (here:square) can be used
result = list(map(square,num))
print(result)
