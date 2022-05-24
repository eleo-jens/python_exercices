"""Créez un script qui demande à l’utilisateur un mot.
Ensuite donner à l’utilisateur le nombre de voyelle de ce mot.
Indice: vous pouvez établir la liste des voyelles facilement ["a", "e", "i", "o", "u", "y"] 
et nous avons vu un moyen de vérifier qu’un élément se trouve dans un groupe.
"""

voyels = ["a","e","i","o","u","y"]
word = input("Donnez moi un mot: ")
count = 0

for letter in word:
    if letter in voyels:
        count = count + 1
print(f"Il y a {count} voyelles dans ce mot")

""" for x in range(len(word)):
    if word[x] in voyels:
        count = count + 1 """