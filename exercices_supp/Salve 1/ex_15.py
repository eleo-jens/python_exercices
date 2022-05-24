""" Écrivez un script qui demande à l’utilisateur un entier entre 1 et 100, 
redemandez tant que l’utilisateur ne donne pas un entier entre 1 et 100.
Ensuite affichez la somme des chiffres de 1 à l’entier donné par l’utilisateur.
Si l’utilisateur vous donne 10, la somme affichée sera 55 car 55 est la somme des entiers de 1 à 10. """

n = 0
res = 0

while n < 1 or n > 100:
    n = int(input("Donnez un chiffre de 1 à 100: "))

for i in range(1, n+1):
    res = res + i
print(res)


#quand on doit chercher si un chiffre est entre deux bornes, c'est mieux de comparer que d'utiliser le in


""" A mathematical way 
n = int(input("Donnez un chiffre de 1 à 100: "))
print(int((n * (n + 1))/2))
"""

""" Another way not optimize bc we stock in an array without reason
list_number = []

for i in range(n+1):
    list_number.append(n)
print(sum(list_number))
"""