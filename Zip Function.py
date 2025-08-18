"""
Zip function is a group of some list/function. It is used for zipping.
Format of zip function:
variable = zip(list1,list2,list3)
"""
roll = [101, 102, 103, 104, 105]
name = ["Anisul", "Rahat", "Rafin", "Sajid", "Nahidul"]

name_roll = list(zip(roll, name, "ASDGG"))
print(name_roll)