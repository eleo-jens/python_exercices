def print_tab(tab):
    for line in range(len(tab)):
        txt = f"{line} "

        for column in range(len(tab[line])):
            txt += tab[line][column] + " "
        print(txt)
        # print("")
    
    txt = "  "
    for column in range(len(tab[0])):
        txt += f"{column} "
    print(txt)

    # def print_tab(tab):
    #     for line in tab:
    #         txt = ""
    #         for element in line:
    #             txt += element + " "
    #         print(txt)

def check_victory_vertical(tab,line,col):

    if line < 3 and tab[line][col] == tab[line + 1][col] and tab[line][col] == tab[line + 2][col]:
        return True
    return False

def check_victory_horizontal(tab, line, col):
    if col > 1 and tab[line][col] == tab[line][col -1] and tab[line][col] == tab[line][col -2]:
        return True

    if col < 3 and tab[line][col] == tab[line][col +1] and tab[line][col] == tab[line][col +2]:
        return True

    if col > 0 and col < 4 and tab[line][col] == tab[line][col +1] and tab[line][col] == tab[line][col -1]:
        return True

    return False

def check_victory_diagonal(tab, line, col):
    
    if line < 3 and col < 3 and tab[line][col] == tab[line +1][col+1] and tab[line][col] == tab[line+2][col+2]:
        return True

    if line > 1 and col > 1 and tab[line][col] == tab[line -1][col-1] and tab[line][col] == tab[line-2][col-2]:
        return True
    
    if col > 0 and col < 4  and line > 0 and line < 4 and tab[line][col] == tab[line-1][col -1] and tab[line][col] == tab[line+1][col+1]:
        return True

    if line < 3 and col > 1 and tab[line][col] == tab[line +1][col-1] and tab[line][col] == tab[line+2][col-2]:
        return True

    if line > 1 and col < 3 and tab[line][col] == tab[line -1][col+1] and tab[line][col] == tab[line-2][col+2]:
        return True
    
    if col > 0 and col < 4 and line < 4 and line > 0 and tab[line][col] == tab[line-1][col +1] and tab[line][col] == tab[line+1][col-1]:
        return True
    return False

# si le nom de la fonction est formulee comme une question ou part check on saura d'avance que la fonction renvoi true or false
def check_victory(tab, col):
    #  1-  Trouver la derniere ligne jouee
    line = 0
    for l in range(len(tab)):
        if tab[l][col] != ".":
            line = l
            break
    # 2 - Check vertical
    if check_victory_vertical(tab, line, col):
        return True
    elif check_victory_horizontal(tab, line, col):
        return True
    else:
        return check_victory_diagonal(tab, line, col)

def place_toker(tab, player, col):
    # bcp de langage pour chaque niveau d'ndentation
    if player == 1:
        token = "O"
    else:
        token = "X"
    
    # 4, 3, 2, 1, 0 car -1 non inclu
    # for line in range(-1, -len(tab) -1, -1) // idem
    for line in range(len(tab)-1, -1, -1):
        if tab[line][col] == ".":
            tab[line][col] = token
            break
    
    return(tab)

def tab_is_full(tab):
    
    for value in tab[0]:
        if value == ".":
            return False
    return True

def give_empty_tab():
    line_number = 5
    column_number = 5

    tab = []
    for i in range(line_number):
        line = []
        for j in range(column_number):
            line.append(".")
        tab.append(line)
    
    return tab

# line_number = 5
# column_number = 5
# num = 0

# tab = []
# for i in range(line_number):
#     line = []
#     for j in range(column_number):
#         line.append(".")
#     tab.append(line)

tab = give_empty_tab()

# tab = [["."] * 5] * 5 

winner = None
current_player = 1

while winner == None:
    # 1 - current_player joue
    print_tab(tab)

    col = int(input(f"Joueur {current_player}, quelle colonne ? "))
    while col < 0 or col >= 5:
        col = int(input(f"Joueur {current_player}, quelle colonne ? "))
    
    place_toker(tab, current_player, col)

    # 2 - verifier si le current_player a gagne. Si pas de gagnant, on verifie si la grille est rempli, dans ce cas on reset une grille vide pour recommencer le jeu
    # revient au meme que check_victory(current_player, tab) == True:
    if check_victory(tab, col):
        winner = current_player
    
    if winner == None:
        if tab_is_full(tab):
            tab = give_empty_tab()

    # 3 - changer le current_player
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1

print_tab(tab)
print(f"Bravo Joueuse.eur {winner} !")
