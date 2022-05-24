# Changer encore la fonction précédente en lui ajoutant un autre argument qui
# représentera cette fois une liste de lettres autorisées.
# Changer le code de la fonction pour que la liste passée en paramètre soit utilisée
# à la place de celle déclarée dans la fonction.


# ecouter la correction de cet exercice

from random import randint

def give_word(n: int, letters: list) -> str:

    word = ""
    if n > len(letters):
        n = len(letters)

    for _ in range(n):
        letter = letters[randint(0, len(letters) - 1)]
        word = word + letter
        letters.remove(letter)
    return word

n = int(input("Give a number of letters : "))
letters = list(input("Give letters to compose a random word (ex: ajhdh): "))
# letters = ["a","i", "l", "n", "o", "r", "s", "t"]
word = give_word(n, letters)

print(word)
