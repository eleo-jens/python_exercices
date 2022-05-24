""" Dans un autre script:
Créez un programme qui va demander à l’utilisateur d’entrer des nombres.
Le programme continuera à en demander tant que l’utilisateur n’aura pas donner deux nombre identique d’affilée.
En fin de programme, affichez la somme des nombres donné par l’utilisateur """

number_1 = int(input("Give a number: "))
number_2 = None
res = 0

while number_1 != number_2:
    number_2 = number_1
    res = res + number_2
    number_1 = int(input("Giver a number: "))
print(res)
