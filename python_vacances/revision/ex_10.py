""" Dans un autre script:
Demandez à l’utilisateur d’entrer des nombre jusqu’à ce qu’il donne la valeur 0.
Ensuite, affichez le plus grand et le plus petit nombre que l’utilisateur a donné."""

number = int(input("Donne un nombre: "))
min = 0
max = 0
while number != 0:
    if number < min:
        min = number
    elif number > max:
        max = number
    number = int(input("Donne un nombre: "))
print(min)
print(max)

