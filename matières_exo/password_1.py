password = "Pyth0n"
#stocker le mot de dans une variable est plus pratique si jamais on doit changer le MDP ou dans le developpement
#mobile ou de jeu vidéo ca permet de gagner de lespace et du temps car chaque chaine de caractère est stocker dans la mémoire ("""  pour les paragraphes """)
user_password = input("Entrez le mot de passe: ")
if user_password != password:
    print("Code éronné.")
else:
    print("Code correct.")