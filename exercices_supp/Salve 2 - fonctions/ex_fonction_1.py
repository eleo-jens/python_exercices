def ft_reverse(word):
    reversed_word = ""

    for letter in word:
        reversed_word = letter + reversed_word
    return reversed_word

word = input("Donnez moi un mot: ")
print(ft_reverse(word))

""" Other ways
def ft_reverse(word):

    reversed_word = ""
    for i in range(-1, -len(word)-1, -1):
        reversed_word = reversed_word + word[i]
    return reversed_word

def ft_reverse(word):
    return word[-1:(len(word)*-1)-1:-1] """

""" Pour les string, on ne peut faire que de la concatenation : Ne fonctionne pas sur les string mais sur une liste oui, on ne peut pas écrire sur une chaine 
par exemple: a = "Eleonore" et je veux faire a[1] = "b": ca ne fonctionne pas 
def ft_reverse(word):

    i = 0
    j = len(word)-1
    reversed_word = ""
    while i < len(word):
        reversed_word[i] = word[j]
        i = i + 1
        j = j - 1
    return reversed_word """
