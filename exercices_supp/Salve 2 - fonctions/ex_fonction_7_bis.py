# Changer la fonction précédente en lui ajoutant un argument qui représentera le
# nombre de lettre du mot.
# Changer le code de la fonction pour que le nombre de lettre du mot généré ne
# soit plus 5, mais le nombre passé en paramètre.

from random import randint

def give_word(n):

    letters = ["a","i", "l", "n", "o", "r", "s", "t"]
    word = ""
    if n > len(letters):
        n = len(letters)

    for _ in range(n):
        letter = letters[randint(0, len(letters) - 1)]
        word = word + letter
        letters.remove(letter)
    return word

n = int(input("Give a number of letters : "))
word = give_word(n)

print(word)