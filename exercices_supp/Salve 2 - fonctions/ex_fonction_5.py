def count_letters(word, letter):
    count = 0
    for i in range(len(word)):
        if word[i] == letter:
            count = count + 1
    return(count)

word = input("Un mot: ")
letter = input("Une lettre: ") 
print(str(count_letters(word, letter)))

""" 
def count_letters(word, letter):
    count = 0
    for caracter in word:
        if caracter == letter:
            count = count + 1
    return(count) """
