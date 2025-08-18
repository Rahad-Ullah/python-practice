import re
pattern = r"color"
text = "This is green color. I love green color."

#match method
if re.match(pattern, text):
    print("Match")
else:
    print("Not match")

#search method
if re.search(pattern, text):
    print("Match")
else:
    print("Not match")

#findall method   #this method publish his search result as a list
expl = re.findall(pattern, text)
print(expl)

#sub or replace method
t1 = re.sub(pattern, "colour", text)
print(t1)

#More on search function
match = re.search(pattern, text)
if match:
    print(match.start())    #this method print the staring index
    print(match.end())      #this method print the end index
    print(match.span())     #this method print the both start and end index