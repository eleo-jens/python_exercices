# Écrivez une autre fonction qui reçoit une liste de prix en paramètre et qui
# renvoie la somme des éléments de cette liste auquel on ajoute la TVA.
# Pour calculer la TVA, utilisez la fonction précédemment créée.

def tvac(price):
    return price * 1.21

# ici c'est plus court car je fais d'abord la somme des elements avec la fonction sum puis j'applique la tva
def sum_tvac(prices):
    return tvac(sum(prices))

print(sum_tvac([12,2,20]))

# ici c'est plus long car je fais la somme apres avoir applique la tva sur chaque element de la liste
# def sum_tvac(price_list):
#     sum = 0
#     for element in price_list:
#         sum = sum + tvac(element)
#     return sum
