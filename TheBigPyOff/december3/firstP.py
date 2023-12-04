import numpy as np

grid = list(list())

maxRow = 0

maxCol = 0

sum = 0

def printGrid(grid):
    for line in grid:
        print(line)

def isConor(x, y):
    if((x == 0 and y == 0) or (x == maxCol and y == 0) or (x == 0 and y == maxRow) or (x == maxCol and y == maxRow)):
        return True
    else:
        return False

def hasDiagonalStart(x, y):
    if(y != 0 and x != 0 and isSym(x-1,y-1)):
        up = True
    else: 
        up = False
    
    if(y != maxRow and x != 0 and isSym(x-1,y+1)):
        down = True
    else: 
        down = False
    
    # print(f"DigUpStart: {up}")
    # print(f"DigDownStart: {down}")
    
    if up or down: return True 
    else: return False

def isSym(x,y):
    if(grid[y][x] == '.' or grid[y][x].isnumeric()):
        return False
    else: 
        return True

def isDot(x,y):
    return grid[y-1][x+1] == '.'

def hasDiagonalEnd(x, y):
    if(y != 0 and x != maxCol and isSym(x+1,y-1)):
        up = True
    else: 
        up = False
    
    if(y != maxRow and x != maxCol and isSym(x+1,y+1)):
        down = True
    else: 
        down = False

    # print(f"DigUpEnd: {up}")
    # print(f"DigDownEnd: {down}")

    if up or down: return True 
    else: return False

def nextToStart(x,y):
    if(x != 0 and isSym(x-1,y)):
        return True
    else:
        return False 
        

def nextToEnd(x,y):
    if(x != maxCol and isSym(x+1,y)):
        return True
    else:
        return False 

def up(x,y):
    if(y != 0 and isSym(x, y-1)):
        return True
    else:
        return False

def down(x,y):
    if(y != maxRow and isSym(x, y+1)):
        return True
    else:
        return False


with open("input/input.txt", 'r') as file:
    for line in file:
        l = list(line.strip())
        maxCol = len(l)-1
        grid.append(l)
        maxRow = len(grid)-1
print(maxRow)
print(maxCol)

def checkDig(x1,x2,y):
    if(hasDiagonalStart(x1,y) or hasDiagonalEnd(x2,y) or nextToStart(x1, y) or nextToEnd(x2, y)):
        return True
    else:
        return False

def checkOther(x,y):
    if (up(x,y) or down(x,y)):
        return True
    else: 
        return False

def check(indexes, number, added):
    print("check")

        
    dig = checkDig(indexes[0], indexes[-1], y)
    # print(number)
    # startDig = hasDiagonalStart(number[0],y)
    # print(startDig)  
    # endDig = hasDiagonalEnd(number[-1],y)
    # print(endDig)
    # nextStart = nextToStart(number[0], y)
    # #print(nextStart)
    # nextEnd = nextToEnd(number[-1], y)
    #print(dig)
    if dig:
        added = True
        print(f"is diagonal, start or end - adds number: {number}") 
        return int(number)

    if not added: 
        for num in indexes:
            upOrDown = checkOther(num, y)
            if(upOrDown): 
                print(f"is other - adds number {number}")
                return int(number)
    return 0


for y, line in enumerate(grid):
    indexes = list()
    number = ""
    #print(f"y: {y}")
    added = False
    for x, item in enumerate(line):
        #print(f"item: {item}")
        #print(f"x: {x}")
        if item.isnumeric():
            indexes.append(x)
            number += item
        else:
            if len(indexes) > 0:
                print(number)
                
                sum += check(indexes, number, added)
                indexes = list()
                number = ""
        
        if(len(indexes) > 0 and x == maxCol):
            sum += check(indexes, number, added)
            indexes = list()
            number = ""

        #print(upOrDown)
        # added = False
        # indexes = list()
        # number = ""
print(sum)

#printGrid(grid)