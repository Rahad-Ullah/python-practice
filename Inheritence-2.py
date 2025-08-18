#Inheritence means finding one class into another class.
class Phone:
    def call(self):
        print("You can call.")
    def message(self):
        print("You can message.")

class Samsung(Phone):
    def photo(self):
        print("You can take photo.")

# Here, 'Phone' is called superclass and 'Samsung' is called subclass of Phone.
print(issubclass(Samsung, Phone))

p = Phone()
p.call()
p.message()

s = Samsung()
s.call()
s.photo()

