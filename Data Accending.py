data_list = [1,5,3,7,2]
new_list = []
while data_list:
    maximum = data_list[0]
    for i in data_list:
        if i>maximum:
            maximum = i
    new_list.append(maximum)
    data_list.remove(maximum)
print(new_list)