def multiplication(number):
    for i in range(1,11):
        result = str(i*number)
        message = str(i) + "x" + str(number) + "=" + result
        print(message)

number = int(input("Chiffre: "))
multiplication(number)