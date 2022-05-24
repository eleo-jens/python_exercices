# Écrivez une fonction qui prend qui ajoute la TVA à un prix donné en paramètre.
# La TVA sera toujours de 21%.
# Exemple: Si la fonction reçoit 2, elle renverra 2.42 car 2 + 2 * 0.21 = 2.42

def tvac(price):
    return price * 1.21

print(tvac(20))

# MA VERSION PLUS LONGUE: car revient au meme de faire * 1.21
# def tvac(price):
#     TVA = 0.21
#     price = price + price * TVA
#     return price