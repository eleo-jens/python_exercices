my_list = [1, 2, 3, 4, 5]
print(my_list)
index = 0
deleted_element = None

# while my_list != []:
# while len(my_list) > 0:
while my_list:
    deleted_element = my_list.pop(index)
    print(deleted_element)
    print(my_list)

