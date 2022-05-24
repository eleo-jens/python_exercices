'''
Dans le même script: 
Si le nombre qui se trouve dans la variable number est plus grand que 10, affichez la chaîne de caractères “Ce nombre est plus grand que 10”.
'''

n = input("Donnez moi un nombre: ")
n = int(n)

print("Votre nombre est " + str(n))

if n > 10:
    print("Ce nombre est plus grand que 10")
