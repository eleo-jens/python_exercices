# Écrivez une fonction qui a une liste et un caractère comme arguments.
# La fonction va placer le caractère dans la dernière case (celle avec l’index le plus
# grand) qui est rempli par un ".".
# Après coup la fonction retournera la liste.
# Dans votre programme principale, utilisez la fonction pour remplir une liste
# remplie avec 6 ".".
# Faites donc en sorte de jouer la fonction tant que la liste n’est pas remplie.
# Après chaque exécution de la fonction, affichez la liste.


# regarder la correction de cet exo

def replace_by_char(letter, suite):
    # ici je parcours la liste a l'envers, la liste a une longueur de 6: ici on part de -1 donc la fin, jusque -7 soit une longueur de 6
    for index in range(-1, -1 - len(suite), -1):
        if suite[index] == '.':
            suite[index] = letter
            return suite

suite = ["."] * 6

while "." in suite:
    suite = replace_by_char("x", suite)
    print(suite)
