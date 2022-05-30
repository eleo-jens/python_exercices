from random import randint

# Etape 1: générer un code aléatoire de 4 lettres et le stocker dans une liste
letters = ["🔴", "🟡", "🟢", "🔵", "🟣", "⚪"]
max = len(letters) - 1
code = []
user_code = []
trails = 0

# on veut passer 4 fois dans la boucle: la longueur de la sequence determine cb de fois on passe dans la boucle; i va valoir 0, 1, 2, 3 et avant 4 du coup cela s'arrete
# i ici est une variable qui n'est pas réutilisée; comme convention on peut appeler cette variable _ pour savoir qu'il n'y a rien à chercher dans le code
for i in range(4):
    index = randint(0, max) 
    code.append(letters[index])

print(code)

# Etape 4: créer une boucle va répéter les étapes de proposition et vérification jusqu'a ce que ca soit correct
while user_code != code and trails != 12: # while len(good_place) != len(code)

    # Etape 2: Demander à l'utilisateur une proposition de code de longueur égale au code de référence
    user_code = list(input("Devinez le code à 4 lettres parmi " + str(letters) + ": "))
    while len(user_code) != len(code): 
        user_code = input("Devinez le code à 4 lettres parmi a, b, c, d, e, f: ")

    user_code = list(user_code)
    print(user_code)

    # Etape 3: déterminer combien de lettres sont exactement bien placées
    good_place = []
    for index in range(len(code)):
        if code[index] == user_code[index]: #and user_code[x] != good_place[x]
            good_place.append(index)
    print("Nombre d'emplacement correct: " + str(len(good_place)))
    print(good_place)

    # Etape 5: vérifier si la lettre est mal placée: en comparant lettre par lettre si elles sont égales, déjà bien placées ou déjà mal placées et les stocker si necessaire dans la liste de mal placées
    wrong_place = []
    for i_user in range(len(user_code)):
        for i_code in range(len(code)):
            #print(str(i_user) + " " + str(i_code))
            if user_code[i_user] == code[i_code] and i_code not in good_place and i_user not in good_place and i_code not in wrong_place:
                #print("Match!")
                wrong_place.append(i_code)
                break
    print("Nombre de lettres mal placées: " + str(len(wrong_place)))
    print(wrong_place)
    
    # Etape 6: intégrer un compteur et une condition de nombre d'essaies
    trails = trails + 1
    print("Tentatives: " + str(trails))

if trails == 12:
    print("Perdu !")
else:
    print("Bien joué !")