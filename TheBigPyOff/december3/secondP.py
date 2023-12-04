
grid = list(list())

maxRow = 0

maxCol = 0

sum = 0

indexes = list(list())

numbers = list(list())

with open("input/test.txt", 'r') as file:
    for line in file:
        l = list(line.strip())
        maxCol = len(l)-1
        grid.append(l)
        maxRow = len(grid)-1
print(maxCol)
print(maxRow)
#79619403
#79841031
for y, line in enumerate(grid):
    #print(f"y: {y}")
    id = list()
    num = ""
    for x, item in enumerate(line):

        if item.isnumeric():
            id.append(x)
            num += item

        if((len(id) > 0 and x == maxCol) or len(id)>0 and not item.isnumeric()):
                indexes.append((y, id, int(num)))
                id = list()
                num = ""


def getCoord(y,x):
    coords = list()
    #print(f"y: {y}, x{x}")
    #conors
    if(y == 0 and x == 0):
        coords.append((y+1,x))
        coords.append((y,x+1))
        coords.append((y+1,x+1))
        return coords
    if(y == 0 and x == maxCol):
        coords.append((y+1,x))
        coords.append((y,x-1))
        coords.append((y+1,x-1))
        return coords
    if(y == maxRow and x == 0):
        coords.append((y-1,x))
        coords.append((y,x+1))
        coords.append((y-1,x+1))
        return coords
    if(y == maxRow and x == maxCol):
        coords.append((y-1,x))
        coords.append((y,x-1))
        coords.append((y-1,x-1))
        return coords
    #first row
    if(y == 0):
        coords.append((y,x-1))
        coords.append((y,x+1))
        coords.append((y+1,x))
        coords.append((y+1,x+1))
        coords.append((y+1,x-1))
        return coords
    #last row
    if(y == maxRow):
        coords.append((y,x-1))
        coords.append((y,x+1))
        coords.append((y-1,x))
        coords.append((y-1,x+1))
        coords.append((y-1,x-1))
        return coords
    if(x == 0):
        coords.append((y-1,x))
        coords.append((y+1,x))
        coords.append((y,x+1))
        coords.append((y-1,x+1))
        coords.append((y+1,x+1))
        return coords
    if(x == maxCol):
        coords.append((y-1,x))
        coords.append((y+1,x))
        coords.append((y,x-1))
        coords.append((y-1,x-1))
        coords.append((y+1,x-1))
        return coords
    
    coords.append((y-1,x))
    coords.append((y+1,x))
    coords.append((y,x+1))
    coords.append((y,x-1))
    coords.append((y-1,x+1))
    coords.append((y-1,x-1))
    coords.append((y+1,x+1))
    coords.append((y+1,x-1))
    return coords

def find(coords):
    num = list()
    usedCoord = list()
    for coord in coords:
        y, x = coord
        for id in indexes:
            yId, xIds, numId = id

            if((y == yId and x in xIds and (yId, xIds) not in usedCoord)):
                usedCoord.append((yId, xIds))
                num.append(numId)
                continue
                
                
                
    print(f"numbers with *: {num}")
    if(len(num) == 2):
        return (num[0],num[1])
    else:
        return(0,0)

star = 0
for y, line in enumerate(grid):
    for x, item in enumerate(line): 
        if (item == '*'):
            coords = getCoord(y,x)
            #print(coords)
            a , b = find(coords)
            print(f"a:{a}, b: {b}")
            sum += (a*b)
print(sum)
#print(star)

def printLists(indexes):
    for id in indexes:
        print(f"index: {id}")






printLists(indexes)
