number = int(input("Entrez un nombre entre 1 a 10: "))
while number < 1 or number > 10:
    number = int(input("Entrez un nombre entre 1 a 10: "))

for i in range(1, 11):
    print(f"{i} x {number} = {i*number}")
