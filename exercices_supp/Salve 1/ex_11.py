""" Dans un autre script:
● Générez deux nombres aléatoire (entre 0 et 100)
● Affichez ces deux nombre en demandant à l’utilisateur d’en donner la somme
● Continuez à lui demander tant que la réponse est mauvaise.
● A la fin du programme, affichez à l’utilisateur le nombre d’erreurs qu’il a commises. """

from random import randint

n1 = randint(0, 100)
n2 = randint(0, 100)

somme = n1 + n2
user_somme = int(input(str(n1) + " + " + str(n2) + " =  ... ? "))
error = 0

while user_somme != somme:
    user_somme = int(input(str(n1) + " + " + str(n2) + " =  ... ? "))
    error += 1
print("Nombre d'erreurs : " + str(error))