grid = list(list())

maxRow = 0

maxCol = 0


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
                startCoord=(1,1)
            grid.append(l)
    return startCoord

def printGrid():
    for line in grid:
        for item in line:
            print(item,end="")
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

def run(startCoord, debug=False):
    nextCoords = (0,0)
    currentCoords = startCoord
    if not debug:
        current = "L"
        prev = (startCoord[0]+1,startCoord[1])
    else: 
        current = "F"
        prev = (startCoord[0],startCoord[1]+1)
    
    steps = 0
    if debug:
        print(f"startNode: {currentCoords}")
        print(f"stat prev: {prev}")
    while(nextCoords != startCoord):
        nextCoords = getNextSpot(prev, current, currentCoords)
        if debug: 
            print(f"prev coords: {prev}")
            print(f"next coords: {nextCoords}")
        prev = currentCoords
        x,y = nextCoords
        next = grid[y][x]
        current = next
        currentCoords = nextCoords
        steps +=1
    
    return steps/2 

startCoord = read("")
printGrid()
debug = False
print(run(startCoord, debug))
