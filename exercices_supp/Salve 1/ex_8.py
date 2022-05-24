""" Écrivez un script qui demande à l’utilisateur un mot de passe.
Si le mot de passe entré n’est pas "Pyth0n" le programme demande à nouveau le mot de passe.
Quand le mot de passe est bon, le programme affiche "Mot de passe valide."
Après 3 tentatives infructueuses, le programme affiche "Mot de passe incorrect." """

password = "Pyth0n"
user_password = None
i = 0

while user_password != password and i < 3: 
    user_password = input("Entrez votre mot de passe: ")
    i = i + 1
if user_password == password:
    print("Mot de passe valide.")
else:
    print("Mot de passe incorrect.")