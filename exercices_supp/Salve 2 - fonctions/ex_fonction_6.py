def remove_vowels(word):
    vowels = ["a","e","i","o","u","y"]
    new_word = ""
    for i in range(len(word)):
        if word[i] not in vowels:
            new_word = new_word + word[i]
    return new_word

word = input("Give a word: ")
print(f"Mot sans voyelles: {remove_vowels(word)}")

# autre version 
# def remove_vowels(word):
#     vowels = ["a","e","i","o","u","y"]
#     new_word = ""
#     for letter in word:
#         if letter not in vowels:
#             new_word += letter
#     return new_word
