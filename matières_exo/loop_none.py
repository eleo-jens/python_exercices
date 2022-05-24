n = None

while n == None or n <= 10:
        n = input("Donne un nombre supérieur à 10: ")
        n = int(n)

print("Chiffre " + str(n))


#autre écriture sans None

n = input("Donne un nombre supérieur à 10: ")
n = int(n)

while n <= 10:
        n = input("Donne un nombre supérieur à 10: ")
        n = int(n)

print("Chiffre " + str(n))