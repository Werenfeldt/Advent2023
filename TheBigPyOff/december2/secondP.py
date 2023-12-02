import numpy

red = 12
green = 13
blue = 14

cubeList = dict()

sum = 0

with open("input.txt", 'r') as file:
    for line in file:
        #get gameid
        gameId, cubeLine = line.split(":")
        id = int(gameId.split(" ")[1].strip())

        #split such that only color and number is back. We dont care about the different draws here
        cubeGames = cubeLine.strip().replace(",", ";").split(";")
        print(cubeGames)

        for cube in cubeGames:
            number, color = cube.strip().split(" ")

            #add the biggest number for the respective colors in dict
            if color not in cubeList:
                cubeList[color] = int(number)
            else:
                cubeList[color] = max(cubeList.get(color),int(number))
        
        #multiply the numbers for the game, and add it to the sum
        values = list(cubeList.values())
        mul = numpy.prod(values)
        sum += mul

        cubeList = dict()

print(sum)

        
