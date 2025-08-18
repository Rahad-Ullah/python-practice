#Stack
books = []
books.append("Learn C")
books.append("Learn C++")
books.append("Learn Java")
print(books)

books.pop()
print("The top book is: ", books[-1])
books.pop()
print("The top book is: ", books[-1])
books.pop()
if not books:
    print("No books left")

# Queue
from collections import deque

bank = deque(["X", "Y", "Z"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()
if not bank:
    print("No customer left")

