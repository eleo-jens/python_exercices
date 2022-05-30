from random import randint

elements = ["a", "b", "c", "d", "e", "f"]
max = len(elements) - 1
my_list = []
my_list_lenght = 4

while len(my_list) != my_list_lenght:
    random_index = randint(0, max) 
    new = elements[random_index]
    my_list.append(new)
print(my_list)