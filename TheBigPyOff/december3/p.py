grid = list(list())

maxRow = 0

maxCol = 0

with open("input/test.txt", 'r') as file:
    for line in file:
        l = list(line.strip())
        maxCol = len(l)-1
        grid.append(l)
        maxRow = len(grid)-1

for y, line in enumerate(grid):
    number = list()
    for x, item in enumerate(line):
        print(f"y: {y}, x: {x}")
        print(f"value: {grid[y][x]}")