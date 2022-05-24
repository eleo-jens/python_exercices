from random import randint

elements = ["poire","pomme","banane","kiwi","cerise","fraise"]

end_list = len(elements) - 1 #on aurait pu mettre 5 mais eviter le hard-coding
# une autre façon de trouver la fin de la liste en utilisant un index négatif -1 (pour le dernier) -2 (pour l'avant dernier)
print(elements[-1])

index = randint(0, end_list)

print(elements)
print(elements[index])
print(elements[1:4])
print(elements[:3]) # prend les premiers éléments avant le 3e index // du début jusqu'à l'index 3 non-inclus
print(elements[4:]) # prend les derniers éléments à partir du 4e index inclus (donc ne prends pas les 4 premiers index) // du 4e index inclu jusqu'à la fin

#une facon de couper une liste en deux en mettant le même nombre
print(elements[:3]) 
print(elements[3:])

print(elements[0:5:2]) # va prendre de l'index 0 à 5 non inclus, en prenant un élément sur 2, en avant pas 2
print(elements[:]) # prend tout (un peu inutile)
print(elements[::2]) # affiche la liste par pas de 2
print(elements[::-1]) #affiche la liste par la fin: inverse
print(elements)

