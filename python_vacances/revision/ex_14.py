""" Ecrire un script qui demande à l’utilisateur un mot.
Tant que le mot n’est pas "end" le script redemandera un mot à l’utilisateur.
A chaque fois que le mot commence par "t" afficher le suivi de "!!!" 
(rappelez-vous que pour lire un seul caractère d’une chaîne de caractère, on doit lui donner son index (comme pour les listes)).
A la fin du script, affichez le nombre de mots entrés par l’utilisateur. """

word = input("Give a word: ")
count = 1

while word != "end":
    count = count + 1
    if word[0] == "t":
        print(word + " !!!")
    word = input("Give a word: ")
print(count)
    