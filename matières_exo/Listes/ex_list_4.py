my_list = []

stop_word = "stop"
index = 0
user_word = input("Entrez un mot ou tapez \"stop\" pour finir: ")

while user_word != stop_word:
    index = int(input("Entrez l'index où le mot doit s'insérer (max:" + str(len(my_list)) + "): "))
    my_list.insert(index, user_word)
    user_word = input("Entrez un mot ou tapez \"stop\" pour finir: ")

print(my_list)