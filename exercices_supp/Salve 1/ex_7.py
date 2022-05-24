""" Écrivez un script qui demande à l'utilisateur un nombre (entre 1 et 10).
Tant qu’il ne rentre pas un chiffre entre 1 et 10, le programme demande à nouveau à l’utilisateur un nombre  (entre 1 et 10). """

n = input("Donnez moi un nombre entre 1 et 10: ")
n = int(n)

while n < 1 or n > 10:
    n = input("Donnez moi un nombre entre 1 et 10: ")
    n = int(n)