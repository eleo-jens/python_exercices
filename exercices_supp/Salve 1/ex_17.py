#symbols = ["coeur", "pique", "carreau", "trèfle"]
symbols = ["❤", "♠", "♦", "♣"]
cards = ["as","deux","trois","quatre","cinq","six","sept","huit","neuf","dix","valet","dame","roi"]

for symbol in symbols:
    for card in cards:
        print(card + " de " + symbol)
