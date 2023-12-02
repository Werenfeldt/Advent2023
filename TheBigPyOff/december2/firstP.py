red = 12
green = 13
blue = 14

cubeList = dict()

sum = 0

def check(redNumber, greenNumber, blueNumber):
    if(redNumber != None and redNumber > red): return False
    if(greenNumber != None and greenNumber > green): return False
    if(blueNumber != None and blueNumber > blue): return False
    return True

with open("input/input.txt", 'r') as file:
    for line in file:
        gameId, cubeLine = line.split(":")
        #print (f"game: {gameId}")
        #print(f"cubes: {cubeLine}")
        id = int(gameId.split(" ")[1].strip())
        cubeGames = cubeLine.split(";")
        possible = True
        for game in cubeGames:
            cubes = game.split(",")
            for cube in cubes:
                number, color = cube.strip().split(" ")

                if(cubeList.get(color) != None):
                    cubeList[color] += int(number)
                else:
                    cubeList[color] = int(number)
            #print(cubeList)
            possible = check(cubeList.get("red"), cubeList.get("green"), cubeList.get("blue"))
            #print(possible)
            cubeList = dict()
            if(not possible): break
        print(f"Game possible adding sum?: {possible}")
        if(possible):
            
            sum += id
        
        #print("new game")
print(sum)

        
