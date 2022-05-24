# Ecrivez un programme qui :
# ● Demande à l’utilisateur des mots:
#  ○ Si le mot commence par "p", il entre mot dans une liste
#  ○ Il demande des mots tant que le mot entré n’est pas "stop"
# ● Affiche la liste des mots
# Note : les index, ça marche aussi pour les chaînes de caractères !

word = input("Give a word or type  \"stop \" to close the program: ")
words = []

while word != "stop":
    if word[0] == "p":
        words.append(word)
    word = input("Give a word: ")
print(words)