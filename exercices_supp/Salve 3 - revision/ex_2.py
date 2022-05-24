# Ecrivez un programme qui :
# ● Demande à l’utilisateur un nombre.
# ● Génère un nombre entre 1 et 20 (et le stocke dans une variable)
# ● Si le nombre de l’utilisateur est plus grand ou égal au nombre aléatoire le programme affiche: "success"
# ● Sinon, il affiche: "failure"

from random import randint

user_num = int(input("Give a number: "))
pc_num = randint(1,20)

if user_num >= pc_num:
    print("success")
else:
    print("failure")