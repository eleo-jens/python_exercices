from random import choice

def random_letter():
    letters = ["a","b","c","d","e"]
    letter = choice(letters)
    return letter

word = ""
for i in range(5):
    word = word + str(random_letter())
print(word)