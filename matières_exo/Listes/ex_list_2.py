my_list = ["foot", "yoga", "cricket", "basket", "dance", "judo"]
end_list = len(my_list) - 1

user_nb = input("Donnez moi un nombre entre 0 et " + str(end_list) + " : ")
user_nb = int(user_nb)

while user_nb < 0 or user_nb > end_list:
    user_nb = input("Donnez moi un nombre entre 0 et " + str(end_list) + " : ")
    user_nb = int(user_nb)

print(my_list)
print(my_list[:user_nb]) #// [0:user_nb]
print(my_list[user_nb:]) #// [user_nb:end_list]