# exemple donne avec une liste mais par exemple si on demande 10000,
# ca va prendre un peu plus d'espace qu'avec une varible
# mais dans les deux cas (liste ou variable) ca demande beaucoup en peformance pour l'affichage

n = int(input("Donnez un nombre plus grand que 1: "))
while n < 2:
    n = int(input("Donnez un nombre plus grand que 1: "))

numbers = [1, 2]

for _ in range(n - 2):
    next_number = numbers[-1] + numbers[-2]
    numbers.append(next_number)

message = "Suite de Fibonacci : "

for number in numbers:
    message = message + str(number) + ", "

# pour enlever la virgule et l'esapce en trop
print(message[:-2])