from random import randint

number = int(input("Choisissez un nombre entre 2 et 5 inclu: "))
while number < 2 or number > 5:
    number = int(input("Choisissez un nombre entre 2 et 5 inclu: "))

res = 0
txt = ""
for i in range(number):
    num = randint(0, 20)
    res = res + num
    if i != number-1:
         txt = txt + str(num) + " + "
    else:
        txt = txt + str(num)
count = 0

user_answer = int(input(txt + " = ? "))
while user_answer != res:
    count += 1
    user_answer = int(input(txt + " = ? "))
print("Nombre de mauvaises reponses: " + str(count))
    

