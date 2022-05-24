""" Dans un autre script:
Récupérez un nombre au clavier et stockez-le dans une variable.
Si le nombre récupéré est plus grand ou égale à 10 affichez “Bravo!”.
Sinon, si il est plus grand que 8 affichez “Pas mal.”
Sinon, si le nombre est plus grand que 5 affichez “Mouais, bof”
Et sinon dans les autres cas affichez “Pas terrible” """

n = input("Donnez moi un nombre: ")
n = int(n)

if n >= 10:
    print("Bravo !")
elif n > 8:
    print("Pas mal.")
elif n > 5:
    print("Mouais, bof")
else:
    print("Pas terrible")