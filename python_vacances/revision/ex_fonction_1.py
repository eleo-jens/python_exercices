# Créer une fonction qui prend un mot argument et qui renvoie le mot inversé.
# Dans le programme principale, demandé à l’utilisateur de saisir un mot au clavier
# et affiché le mot inverse.
# Exemple:
# Si le mot est "hologramme" le mot affiché en retour sera "emmargoloh"

import re


def ft_reverse(word):

    reversed_word = ""
    for letter in word:
        reversed_word = letter + reversed_word
    return(reversed_word)

word = input("Give a word: ")
print(ft_reverse(word))
