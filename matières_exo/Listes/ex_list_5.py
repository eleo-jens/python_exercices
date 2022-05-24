my_list = [1, 1, 2, 5, 5, 3, 5, 2, 3]

print(my_list)

user_nb = int((input("Entrez un nombre entre 1 et 5: ")))

my_list.remove(user_nb)

print(my_list)

""" 
Pour retirer toutes les occurences et pas seulement la première
while user_nb in my_list:
    my_list.remove(user_nb) """