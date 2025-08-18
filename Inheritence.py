"""
Inheritance means the reuse of existing code.
"""""

class Phone:
    def call(self):
        print("You can call now.")
    def message(self):
            print("You can message now.")

class Mobile(Phone):
    # 'call' and 'message' function will be attached here automatically.
    def photo(self):
        print("You can take photo now.")

p = Phone()
p.call()
p.message()

m = Mobile()
m.call()
m.message()
m.photo()

# Here: Phone is the parent class /superclass /base class
# and Mobile is the child class /subclass /derived class
print(issubclass(Mobile, Phone))
