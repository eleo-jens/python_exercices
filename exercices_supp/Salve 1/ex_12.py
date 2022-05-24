""" Dans un autre script:
Créez un programme qui va demander à l’utilisateur d’entrer des nombres.
Le programme continuera à en demander tant que l’utilisateur n’aura pas donner deux nombre identique d’affilée.
En fin de programme, affichez la somme des nombres donné par l’utilisateur """

first_n = int(input("Donner un nombre: "))
last_n = None
result = 0

while first_n != last_n:
    last_n = first_n
    result = result + last_n
    first_n = int(input("Donnez un nombre: "))

print("La somme: " + str(result + first_n))