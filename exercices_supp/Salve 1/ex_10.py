""" Dans un autre script:
Demandez à l’utilisateur d’entrer des nombre jusqu’à ce qu’il donne la valeur 0.
Ensuite, affichez le plus grand et le plus petit nombre que l’utilisateur a donné."""

n = int(input("Donnez un nombre: "))
n_min = 0
n_max = 0

while n != 0:
    if n > n_max:
        n_max = n
    elif n < n_min:
        n_min = n
    n = int(input("Donnez un nombre: "))

print("Min: " + str(n_min) + " et Max: " + str(n_max))