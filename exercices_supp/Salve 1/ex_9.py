""" Dans un autre script:
Écrivez un programme qui va générer  trois nombres aléatoirement (entre 1  et 6).
Ensuite le programme va afficher les trois nombres.
Si les trois nombres ne sont pas identiques, il recommence. """

from random import randint
n1 = randint(1, 6)
n2 = randint(1, 6)
n3 = randint(1, 6)

print(n1, n2, n3)

while n1 != n2 or n1 != n3:
    n1 = randint(1, 6)
    n2 = randint(1, 6)
    n3 = randint(1, 6)
    print(n1, n2, n3)
