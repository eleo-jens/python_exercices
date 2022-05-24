# Ecrivez une fonction qui écrit un mot de 5 lettres avec les lettres suivantes: 
# "a","i", "l", "n", "o", "r", "s", "t". Le mot sera ensuite retourné par la fonction.
# Attention les lettres ne peuvent être utilisées qu’une seule fois dans le mot.
# Par exemple: "tsoni" est un mot valide mais pas "liara"

from random import randint

def give_word():

    letters = ["a","i", "l", "n", "o", "r", "s", "t"]
    word = ""

    for _ in range(5):
        letter = letters[randint(0, len(letters) - 1)]
        word = word + letter
        letters.remove(letter)
    return word

for _ in range(5):
    print(f"Mot: {give_word()}")