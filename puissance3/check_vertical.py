# fichier qu'on a utilise pour parvenir a l'algo pour la verification en visualisant la grille

def check_victory_vertical(tab, line, col):

    if line < 3 and tab[line][col] == tab[line + 1][col] and tab[line][col] == tab[line + 2][col]:
        return True
    return False

grid = [[".",".",".",".","."],
        [".",".","X",".","."],
        [".",".","X",".","."],
        [".",".","X","O","."],
        [".",".","O","X","."],]

print(check_victory_vertical(grid, 1, 2))