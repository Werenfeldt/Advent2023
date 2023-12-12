grid = list(list())

colExpansions = list()

rowExpansions = list()

def read(test=""):
    with open(f"input{test}/input.txt", 'r') as file:
        for i, line in enumerate(file):
            l = list(line.strip())
            grid.append(l)
            if "#" not in l:
                colExpansions.append(i)
            #maxRow = len(grid)-1

def printGrid():
    for line in grid:
        for item in line:
            print(f"{item}", end="")
        print("")

def expandVert(debug=False):
    toExpand = list()
    for x in range(len(grid[0])):
        expand = True
        for y in range(len(grid)):
            if "#" == grid[y][x]:
                expand = False
        if expand:
            toExpand.append(x)

    for i, n in enumerate(toExpand):
        rowExpansions.append(n)

def findPoints(debug=False):
    points = list()
    for y, line in enumerate(grid):
        for x, _ in enumerate(line):
            if grid[y][x] == "#":
                points.append((x,y))
    if debug: 
        print(points)
    return (points)


def cal(p1, p2, expansions, debug=False):
    x1,y1 = p1
    x2, y2 = p2
    xHigh = max(x1, x2)
    xLow = min(x1,x2)
    x = x2 - x1 if x2 > x1 else x1 - x2
    y = y2 - y1 if y2 > y1 else y1 - y2
    for num in colExpansions:
        if debug: 
            print(f"num: {num}, y1: {y1}, y2: {y2}")
        if y1 < num and y2 > num:
            y += (expansions-1)
    for num in rowExpansions:
        if debug:
            print(f"num: {num}, x1: {xLow}, x2: {xHigh}")
        if xLow < num and xHigh > num:
            if debug: 
                print("x is between")
            x += (expansions-1)
    return x + y 
    

def shortestPath(point, lst, expansion, debug=False):
    sum = 0
    for p2 in lst: 
        if point != p2:
            l = cal(point, p2, expansion, debug)
            if debug: 
                print(f"point: {point}, p2: {p2}: l: {l}")
            sum += l
    return sum
    
def run(points :list, expansion, debug=False):
    result = 0
    lst = points.copy()
    for point in points: 
        lst.remove(point)
        result += shortestPath(point, lst, expansion, debug)
    return result

read()
debug = False
expandVert(debug)
#print(colExpansions)
#print(rowExpansions)
points = findPoints(debug)
l = run(points, 1000000, debug)
print(l)
#printGrid()