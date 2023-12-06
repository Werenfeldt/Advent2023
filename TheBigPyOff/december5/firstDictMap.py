seedstr = "929142010 467769747 2497466808 210166838 3768123711 33216796 1609270159 86969850 199555506 378609832 1840685500 314009711 1740069852 36868255 2161129344 170490105 2869967743 265455365 3984276455 31190888"

seedToSoil = dict()
soilToFert = dict()
fertToWater = dict()
waterToLight = dict()
lightToTemp = dict()
tempToHumid = dict()
humidToLocation = dict()

def readTest():
    with open("input/test/seedToSoil.txt", 'r') as file:
        for line in file: 
            dis, src, ran = map(int, line.strip().split())
            for i in range(ran):
                seedToSoil[src+i] = dis+i
    with open("input/test/soilToFert.txt", 'r') as file:
        for line in file: 
            dis, src, ran = map(int,line.strip().split())
            for i in range(ran):
                soilToFert[src+i] = dis+i
    with open("input/test/fertToWater.txt", 'r') as file:
        for line in file: 
            dis, src, ran = map(int, line.strip().split())
            for i in range(ran):
                fertToWater[src+i] = dis+i
    with open("input/test/waterToLight.txt", 'r') as file:
        for line in file: 
            dis, src, ran = map(int, line.strip().split())
            for i in range(ran):
                waterToLight[src+i] = dis+i
    with open("input/test/lightToTemp.txt", 'r') as file:
        for line in file: 
            dis, src, ran = map(int, line.strip().split())
            for i in range(ran):
                lightToTemp[src+i] = dis+i
    with open("input/test/tempToHumid.txt", 'r') as file:
        for line in file: 
            dis, src, ran = map(int, line.strip().split())
            for i in range(ran):
                tempToHumid[src+i] = dis+i
    with open("input/test/humidToLoca.txt", 'r') as file:
        for line in file: 
            dis, src, ran = map(int, line.strip().split())
            for i in range(ran):
                humidToLocation[src+i] = dis+i

def read():
    with open("input/seedToSoil.txt", 'r') as file:
        for line in file: 
            dis, src, ran = map(int, line.strip().split())
            for i in range(ran):
                seedToSoil[src+i] = dis+i
    with open("input/soilToFert.txt", 'r') as file:
        for line in file: 
            dis, src, ran = map(int,line.strip().split())
            for i in range(ran):
                soilToFert[src+i] = dis+i
    with open("input/fertToWater.txt", 'r') as file:
        for line in file: 
            dis, src, ran = map(int, line.strip().split())
            for i in range(ran):
                fertToWater[src+i] = dis+i
    with open("input/waterToLight.txt", 'r') as file:
        for line in file: 
            dis, src, ran = map(int, line.strip().split())
            for i in range(ran):
                waterToLight[src+i] = dis+i
    with open("input/lightToTemp.txt", 'r') as file:
        for line in file: 
            dis, src, ran = map(int, line.strip().split())
            for i in range(ran):
                lightToTemp[src+i] = dis+i
    with open("input/tempToHumid.txt", 'r') as file:
        for line in file: 
            dis, src, ran = map(int, line.strip().split())
            for i in range(ran):
                tempToHumid[src+i] = dis+i
    with open("input/humidToLoca.txt", 'r') as file:
        for line in file: 
            dis, src, ran = map(int, line.strip().split())
            for i in range(ran):
                humidToLocation[src+i] = dis+i

def parseSeed():
    seeds = seedstr.strip().split()
    return seeds

def printDicts():
    print(seedToSoil)

def determine(old, new):
    result = old if new == None else new
    return result

def find(seed):
    print(f"seed: {seed}")
    soil = determine(seed, seedToSoil.get(seed))

    print(f"soil: {soil}")
    fert = determine(soil, soilToFert.get(soil))
    
    print(f"fert: {fert}")
    water = determine(fert, fertToWater.get(fert))
    
    print(f"water: {water}")
    light = determine(water, waterToLight.get(water))
    
    print(f"light: {light}")
    temp = determine(light, lightToTemp.get(light))
    
    print(f"temp: {temp}")
    humid = determine(temp, tempToHumid.get(temp))
    
    print(f"humid: {humid}")
    loca = determine(humid, humidToLocation.get(humid))
    print(f"loca: {loca}")
    
    return loca

seeds = parseSeed()
read()
result = list()
for seed in seeds:
    result.append(find(seed))

result.sort()

print(result[0])
#printDicts()
