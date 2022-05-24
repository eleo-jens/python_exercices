from random import randint

def  give_numbers(n):

    my_list =[]

    for i in range(n):
        number = randint(1,6)
        my_list.append(number)
    return(my_list)

n = int(input("Donnez un chiffre: "))
print(str(give_numbers(n)))

""" Other way less optimized
def give_numbers(number):
    integer_list = [1, 2, 3, 4, 5, 6]
    n_list = []
    for i in range(number):
        index = randint(0,len(integer_list)-1)
        n_list.append(integer_list[index])
    return(n_list)

number = int(input("Donnez un chiffre: "))
print(str(give_numbers(number))) """