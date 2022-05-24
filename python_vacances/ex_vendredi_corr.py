from random import randint

number = int(input("Choisissez un nombre entre 2 et 5 inclu: "))
while number < 2 or number > 5:
    number = int(input("Choisissez un nombre entre 2 et 5 inclu: "))

res = 0
txt = ""

for _ in range(number):
    num = randint(0, 20)
    txt = txt + str(num) + " + "
    res = res + num

# le txt[:-2] permet de faire un spliting et donc d'enlever les 2 derniers elements de la chaine a savoir le dernier +
txt = "Donne-moi la somme des nombres suivants: " + txt[:-2] + " = ? "

count = 0

user_answer = int(input(txt))
while user_answer != res:
    count += 1
    user_answer = int(input(txt))

print("Nombre de mauvaises reponses: " + str(count))
    

