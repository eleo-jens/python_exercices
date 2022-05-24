grid = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]

for line in grid:
    txt = ""
    for element in line:
        txt = txt + str(element/2) + " "
    print(txt)

""" grid generator"
grid = []
number_line = 3
column_line = 4
start_num = 1

for line in range(number_line):
    line = []
    for column in range(column_line):
        line.append(start_num)
        start_num += 1
    grid.append(line)

for line in range(3):
    txt = ""
    for column in range(4):
        integer = grid[line][column]
        txt = txt + str(integer/2) + " "
    print(txt)
"""