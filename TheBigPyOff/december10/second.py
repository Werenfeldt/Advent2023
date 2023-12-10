grid = list(list())


def read(test="", debug=False):

    with open(f"input{test}/input.txt", 'r') as file:
        for y, line in enumerate(file):
            l = list(line.strip())
            if not debug:
                if "S" in l: 
                    for x, item in enumerate(l):
                        if item == "S":
                            startCoord=(x,y)
            else: 
                startCoord=(4,12)
            grid.append(l)
    return startCoord

#┌┐└┘
def printGrid(path):
    for y, line in enumerate(grid):
        for x, item in enumerate(line):
            p = item
            #print(path)
            if (x,y) in path:
                match item: 
                    case "F": p = "┌"
                    case "7": p = "┐"
                    case "L": p = "└"
                    case "J": p = "┘"
            print(p,end="")
        print()

def getNext7(coords):
    x,y=coords
    return ((x-1,y),(x,y+1))

def getNextJ(coords):
    x,y=coords
    return ((x,y-1),(x-1,y))

def getNextF(coords):
    x,y=coords
    return ((x,y+1),(x+1,y))

def getNextL(coords):
    x,y=coords
    return ((x,y-1),(x+1,y))

def getNextHori(coords):
    x,y=coords
    return ((x+1,y),(x-1,y))

def getNextVert(coords):
    x,y=coords
    return ((x,y+1),(x,y-1))
  
def updateStartY(coords, old):
    y = coords[1]
    if y < old:
        return y
    else:
        return old

def updateEndY(coords, old):
    y = coords[1]
    if y > old:
        return y
    else:
        return old
    


def getNextSpot(prev, current, currentCoords, debug=False):
    match current: 
        case "7":  
            op1, op2 = getNext7(currentCoords)
            return op1 if op2 == prev else op2
        case "J": 
            op1, op2 = getNextJ(currentCoords)
            return op1 if op2 == prev else op2
        case "F":
            op1, op2 = getNextF(currentCoords)
            return op1 if op2 == prev else op2
        case "L":
            op1, op2 = getNextL(currentCoords)
            return op1 if op2 == prev else op2
        case "-":
            op1, op2 = getNextHori(currentCoords)
            return op1 if op2 == prev else op2
        case "|":
            op1, op2 = getNextVert(currentCoords)
            return op1 if op2 == prev else op2

def getPointsToCompare(lst):
    points = list()
    for i in range(1,len(lst)):
        if lst[i] - lst[i-1] > 1:
            points.append(lst[i-1])
            points.append(lst[i])
    return points
        

def run(startCoord, debug=False):
    path = list()
    nextCoords = (0,0)
    currentCoords = startCoord
    startY = 150
    endY = 0

    if not debug:
        current = "L"
        prev = (startCoord[0]+1,startCoord[1])
    else: 
        current = "F"
        prev = (startCoord[0],startCoord[1]+1)
    

    if debug:
        print(f"startNode: {currentCoords}")
        print(f"stat prev: {prev}")
    while(nextCoords != startCoord):
        nextCoords = getNextSpot(prev, current, currentCoords)
        startY = updateStartY(nextCoords, startY)
        endY = updateEndY(nextCoords, endY)
        
        path.append(nextCoords)
        
        if debug: 
            print(f"prev coords: {prev}")
            print(f"next coords: {nextCoords}")
        prev = currentCoords
        x,y = nextCoords
        next = grid[y][x]
        current = next
        currentCoords = nextCoords
        
    if debug:
        print(f"starty: {startY}, endY: {endY}")
    return (path, startY, endY)


def check(path, debug=False):
    total = 0
    maxX = len(grid[0])
    for i in range(len(grid)):
        for j in range(maxX):
            if debug:
                print(f"looking at: {(j,i)}")
            if (j,i) not in path:
                if debug:
                    print(f"not in path: {(j,i)}")
                determine = 0
                for k in range(j+1,maxX):
                    #if debug:
                        #print(f"looking at: {(k,i)}")
                    if (k,i) in path:
                        if grid[i][k]== "F" or grid[i][k] == "7" or grid[i][k] =="|":
                            
                            determine += 1
                if determine % 2 != 0 and determine != 0:
                    if debug: 
                        print(f"{j,i} INSIDE")
                    total += 1
    return total
        

#tæl kun F og 7 og |
startCoord = read()
debug = False
path, start, end = run(startCoord, debug)
print(path)
printGrid(path)
print(check(path, debug))
#587
#2887