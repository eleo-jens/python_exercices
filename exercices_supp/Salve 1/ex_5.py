# Dans le même script: A la suite de la condition, si celle-ci n’est pas remplie, affichez le message suivant: “Le nombre est plus petit ou égal à 10.” 

n = int(input("Donnez moi un nombre: "))

print("Votre nombre: " + str(n))
if n > 10:
    print("Ce nombre est plus grand que 10.")
else:
    print("Ce nombre est plus petit ou égal à 10.")