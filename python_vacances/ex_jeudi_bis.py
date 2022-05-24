from random import randint

WORDS = ["Pierre", "Papier", "Ciseaux"]

ROCK = 1
PAPER = 2
SCISOR = 3

WIN = "- vous avez gagné !"
FAIL = "- vous avez perdu !"
TIE = "- égalité !"

player = int(input("Entrez 1 pour pierre, 2 pour papier, 3 pour ciseaux: "))
while player < 1 or player > 3:
    player = int(input("Entrez 1 pour pierre, 2 pour papier, 3 pour ciseaux: "))

pc = randint(1,3)

if (player == ROCK and pc == SCISOR) or (player == PAPER and pc == ROCK) or (player == SCISOR and pc == PAPER):
    print(f"Vous: {WORDS[player - 1]}, PC: {WORDS[pc - 1]} {WIN}")

elif (player == pc):
    print(f"Vous: {WORDS[player - 1]}, PC: {WORDS[pc - 1]} {TIE}")

else:
    print(f"Vous: {WORDS[player - 1]}, PC: {WORDS[pc - 1]} {FAIL}")