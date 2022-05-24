def generate_grid(number_line, number_column):
    start = 1 
    grid = []

    for line in range(number_line):
        line = []
        for column in range(number_column):
            line.append(start)
            start += 1
        grid.append(line)
    return(grid)

number_line = 3
number_column = 4
grid = generate_grid(number_line, number_column)

for line in range(number_line):
    txt = ""
    for column in range(number_line):
        txt = txt + " " + str(grid[line][column]/2)
    print(txt)





# CODE EXPLAINED
# number_line = 3
# number_column = 4
# start = 1
# grid = []

# for line in range(number_line):
#         # ici on cree le nombre de sous-liste/ les lignes du tableaux
#         line = []
#         # pour chacune des listes on integrer le nombre start qu'on incremente
#         for column in range(number_column):
#             line.append(start)
#             start = start + 1
#         # on integre chaque sous liste au sein de la grille
#         grid.append(line)
# print(grid)

