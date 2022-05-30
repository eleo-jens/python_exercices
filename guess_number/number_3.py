from random import randint
number = randint(1, 10)

i = 3
while i > 0:
    user_number = input("Donnez moi un nombre entre 1 et 10: ")
    user_number = int(user_number)

    if user_number == number:
        print("Bravo, vous avez trouvé le bon nombre !")
        break
    elif user_number > number:
        print("Votre nombre est trop grand")
    else:
        print("Votre nombre est trop petit")
    i = i - 1
    #print(f"Nombre de vie: {i}")
    if i == 0 and user_number != number:
        print("La réponse est " + str(number))

# 3 façons d'utiliser print: 
# print("Votre nombre (" + user_number + ") est trop grand")
# print("Votre nombre ({}) est trop grand".format(user_number))
# print(f"votre nombre ({user_number}) est trop grand")
