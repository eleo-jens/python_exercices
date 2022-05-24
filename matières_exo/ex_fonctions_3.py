from random import choice

def generate_word(number):
    letters = ["a","h","k","o","n","s","t"]
    word = ""
    
    for i in range(number):
        letter = choice(letters)
        word = word + letter
    return word

number = int(input("Combien de lettre: "))
print(generate_word(number))