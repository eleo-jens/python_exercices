from random import randint
number = randint(1, 10)

user_number = input("Donnez moi un nombre entre 1 et 10: ")
user_number = int(user_number)

i = 1

while user_number != number and i < 3:
    if user_number > number:
        print("Votre nombre est trop grand")
    else:
        print("Votre nombre est trop petit")

    user_number = input("Donnez moi un nombre entre 1 et 10: ")
    user_number = int(user_number)
    i = i + 1

if user_number == number:
    print("Bravo, vous avez trouvé le bon nombre !")
else:
    print("La réponse est " + str(number))