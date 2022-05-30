from random import randint

letters = ["a", "b", "c", "d", "e", "f"]
max = len(letters) - 1
code = []

# on veut passer 4 fois dans la boucle: la longueur de la sequence determine cb de fois on passe dans la boucle; i va valoir 0, 1, 2, 3 et avant 4 du coup cela s'arrete
# i ici est une variable qui n'est pas réutilisée; comme convention on peut appeler cette variable _ pour savoir qu'il n'y a rien à chercher dans le code
for i in range(4):
    index = randint(0, max) 
    code.append(letters[index])

print(code)