from random import randint
number = randint(1, 10)

user_number = input("Donnez moi un nombre entre 1 et 10: ")

if int(user_number) > number:
    print("Votre nombre (" + str(user_number) + ") est trop grand") 
elif int(user_number) == number:
    print("Vous avez deviné le nombre")
else:
    print("Votre nombre (" + str(user_number) + ") est trop petit")