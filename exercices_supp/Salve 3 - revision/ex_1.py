# Ecrivez un programme qui :
# ● Demande à l’utilisateur un nombre.
# ● Génère un nombre entre 1 et 20 (et le stocke dans une variable)
# ● Affiche  "<nombre généré> + <nombre utilisateur> = <somme des deux>"
# Exemple:Si le nombre aléatoire est 6 et le nombre donnée par l’utilisateur est 3 l’affichage sera:"6 + 3 = 9"

from random import randint

user_num = int(input("Give a number: "))
pc_num = randint(1, 20)
res = user_num + pc_num
print(f"{user_num} + {pc_num} = {res}")
