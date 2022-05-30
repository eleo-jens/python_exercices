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




grid_1 = [[".",".",".",".","."],
          [".",".",".",".","."],
          ["X","O",".",".","O"],
          [".","X",".","O","O"],
          ["X","X","X","O","O"],]

grid_2 = [[".",".",".",".","."],
          [".",".",".",".","."],
          ["X","O",".","O",""],
          ["X","X",".","X","X"],
          ["O","O","X","X","O"],]

grid_3 = [[".",".",".",".","."],
          [".",".","X",".","."],
          ["X","X","O","O",""],
          ["X","X",".","X","X"],
          ["O","O","X","X","O"],]

grid_4 = [[".",".",".",".","."],
          [".",".","X",".","."],
          ["X",".","O","O",""],
          ["X","X",".","X","X"],
          ["O","O","X","X","O"],]

assert check_victory_diagonal(grid_1, 2, 0) == True
assert check_victory_diagonal(grid_1, 4, 2) == True
assert check_victory_diagonal(grid_1, 2, 1) == True
assert check_victory_diagonal(grid_3, 3, 0) == True
assert check_victory_diagonal(grid_3, 1, 2) == True
assert check_victory_diagonal(grid_3, 2, 1) == True
assert check_victory_diagonal(grid_4, 1, 0) == True
