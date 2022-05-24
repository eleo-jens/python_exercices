""" Ecrire un script qui demande à l’utilisateur un mot.
Tant que le mot n’est pas "end" le script redemandera un mot à l’utilisateur.
A chaque fois que le mot commence par "t" afficher le suivi de "!!!" 
(rappelez-vous que pour lire un seul caractère d’une chaîne de caractère, on doit lui donner son index (comme pour les listes)).
A la fin du script, affichez le nombre de mots entrés par l’utilisateur. """

word = "end"
count = 1
user_word = input("Entrez un mot: ")

while user_word != word:
    count = count + 1
    if user_word[0] == 't':
        print(user_word + " !!!")
    user_word = input("Entrez un mot: ")
print(count)

""" Autre solution non optimalisée, car ce n'est pas optimal de stocker les mots pour ensuite les compter !
word = "end"
list_word = []
user_sword = input("Entre un mot: ")
i = 0

while user_word != word:
    if user_word[0] == 't':
        print(user_word + " !!!")
    list_word.append(user_word)
    user_sword = input("Entre un mot: ")
    
list_word.append(word)
count = len(list_word)
print(count)
print(list_word)
""" 
