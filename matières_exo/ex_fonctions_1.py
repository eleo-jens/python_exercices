from random import randint

def salutation():

    my_list = ["Bonjour", "Hello", "Ola", "Ciao"]
    index = randint(0, len(my_list)-1)
    print(my_list[index])

""" Other way: from random import random
def salutation():

    my_list = ["Bonjour", "Hello", "Ola", "Ciao"]
    word = choice(my_list)
    return word
"""

""" Other way: import random
def salutation():

    my_list = ["Bonjour", "Hello", "Ola", "Ciao"]
    print(random.choice(my_list)) """

for i in range(100): #ici for est plus approprié que while, car while necessite l'initialisation d'une variable à incrémenter ensuite
    salutation()
    