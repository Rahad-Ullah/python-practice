# X Args
def student(*details):
    print(details)

student("Anisul Islam",102,3.75)

def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)

add(20,30)
add(50,60,30)
add(10,20,30,40)