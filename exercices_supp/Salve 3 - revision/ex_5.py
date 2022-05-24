# Ecrivez un programme qui :
# ● Crée première liste valant [2, 3, 5, 7, 11, 13, 17, 23]
# ● Crée deuxième une liste vide
# ● Vide la première liste et ajoute son contenu dans la deuxième liste, 
#   mais dans l’ordre inverse (donc [23, 17, 13, 11, 7, 5, 3, 2])

first_list = [2, 3, 5, 7, 11, 13, 17, 23]
second_list = []

for i in range(len(first_list)):
    removed = first_list.pop(-1)
    # print(removed)
    # print(first_list)
    second_list.append(removed)
print(second_list)
print(first_list)