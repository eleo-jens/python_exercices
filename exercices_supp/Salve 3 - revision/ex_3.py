# Ecrivez un programme qui :
# ● Demande à l’utilisateur un nombre, et qui continue à demander tant que le nombre n’est pas entre 1 et 5
# ● Génère un nombre aléatoire (entre 1 et 5)
# ● Ensuite le programme affiche le nombre généré avec entre parenthèses la différence entre les deux nombres
# Exemple:Si le nombre aléatoire est 3 et le nombre donnée par l’utilisateur est 5 l’affichage sera:"3 (-2)"

from random import randint

user_num = int(input("Give a number: "))
while user_num < 1 or user_num > 5:
    user_num = int(input("Give a number: "))

pc_number = randint(1, 5)

res = pc_number - user_num

print(f"{pc_number} ({res})")