grid = list(list())


def read(test=""):
    with open(f"input{test}/input.txt", 'r') as file:
        for i, line in enumerate(file):
            l = list(line.strip())
            grid.append(l)
            if "#" not in l:
                grid.append(l.copy())
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
        for line in grid:
            line.insert(n+i, ".")

def findPoints(debug=False):
    points = list()
    for y, line in enumerate(grid):
        for x, _ in enumerate(line):
            if grid[y][x] == "#":
                points.append((x,y))
    if debug: 
        print(points)
    return (points)


def cal(p1, p2):
    x1,y1 = p1
    x2, y2 = p2
    x = x2 - x1 if x2 > x1 else x1 - x2
    y = y2 - y1 if y2 > y1 else y1 - y2
    return x + y 
    

def shortestPath(point, lst, debug=False):
    sum = 0
    for p2 in lst: 
        if point != p2:
            l = cal(point, p2)
            if debug: 
                print(f"point: {point}, p2: {p2}: l: {l}")
            sum += l
    return sum
    
def run(points :list, debug=False):
    result = 0
    lst = points.copy()
    for point in points: 
        lst.remove(point)
        result += shortestPath(point, lst, debug)
    return result

read("/test")
debug = False
expandVert(debug)
points = findPoints(debug)
l = run(points, debug)
print(l)
#printGrid()