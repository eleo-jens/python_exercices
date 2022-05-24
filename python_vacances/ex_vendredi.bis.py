from random import randint

number = int(input("Choisissez un nombre entre 2 et 5 inclu: "))
while number < 2 or number > 5:
    number = int(input("Choisissez un nombre entre 2 et 5 inclu: "))

res = 0
my_list = []
for i in range(number):
    num = randint(0, 20)
    my_list.append(num)
print(my_list)
res = sum(my_list)
print(res)
count = 0

user_answer = int(input(txt + " = ? "))
while user_answer != res:
    count += 1
    user_answer = int(input(txt + " = ? "))
print("Nombre de mauvaises reponses: " + str(count))
    

