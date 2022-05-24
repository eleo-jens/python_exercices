from random import randint

numbers = [1,2,3]
WORDS = ["Pierre", "Papier", "Ciseaux"]

WIN = "- vous avez gagné !"
FAIL = "- vous avez perdu !"
TIE = "- égalité !"

player = int(input("Entrez 1 pour pierre, 2 pour papier, 3 pour ciseaux: "))
while player < 1 or player > 3:
    player = int(input("Entrez 1 pour pierre, 2 pour papier, 3 pour ciseaux: "))

pc = randint(1,3)

#cherche l'index du nombre de l'user et du pc pour pouvoir imprimer ensuite le mot correspondant et non le nombre
index_user = numbers.index(player)
index_prog = numbers.index(pc)

if (player == 1 and pc == 3) or (player == 2 and pc == 1) or (player == 3 and pc == 2):
    print(f"Vous: {WORDS[index_user]}, PC: {WORDS[index_prog]} {WIN}")

elif (player == pc):
    print(f"Vous: {WORDS[index_user]}, PC: {WORDS[index_prog]} {TIE}")

else:
    print(f"Vous: {WORDS[index_user]}, PC: {WORDS[index_prog]} {FAIL}")