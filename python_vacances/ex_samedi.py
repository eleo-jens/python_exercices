number = int(input("Donnez un nombre plus grand que 1: "))
while number < 2:
    number = int(input("Donnez un nombre plus grand que 1: "))

n1 = 0
n2 = 1
suite = ''

for _ in range(number):
    n = n1 + n2
    # le second devient le premier
    n1 = n2
    # la somme devient le second
    n2 = n
    suite = suite + str(n) + " "
print(suite)


# CORRECTION DU PROF
# number = int(input("Donnez un nombre plus grand que 1: "))
# while number < 2:
#     number = int(input("Donnez un nombre plus grand que 1: "))

# first = 0
# seconde = 1
# suite = "1, 2, "

# for _ in range(number):
#     next_number = first + second
#     suite = suite + str(next_number) + " "
#     first = second
#     second = next_number
# print(suite)