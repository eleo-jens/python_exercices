my_list = []

user_word = input("Entrez un mot ou tapez \"stop\" pour finir: ")
stop_word = "stop"

while user_word != stop_word:
    my_list.append(user_word)
    user_word = input("Entrez un mot ou tapez \"stop\" pour finir: ")
print(my_list)