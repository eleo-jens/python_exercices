grid = [["a","b","c"],
        ["d","e","f"],
        ["g","h","i"]]

for line in range(3):
    txt = ""
    for column in range(3):
        txt = txt + grid[line][column]
    print(txt + "\n")

""" Other way: 
for line in grid:
    txt =""
    for element in line:
        txt = txt + element + " "
    print(txt + "\n") """