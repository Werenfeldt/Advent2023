import threading

seedstr = "929142010 467769747, 2497466808 210166838, 3768123711 33216796, 1609270159 86969850, 199555506 378609832, 1840685500 314009711, 1740069852 36868255, 2161129344 170490105, 2869967743 265455365, 3984276455 31190888"
seedstrTest = "79 14, 55 13"

seedToSoil = list()
soilToFert = list()
fertToWater = list()
waterToLight = list()
lightToTemp = list()
tempToHumid = list()
humidToLocation = list()
seeds = list()

def read(test=''):
    with open(f"input{test}/seedToSoil.txt", 'r') as file:
        for line in file: 
            dis, src, ran = map(int, line.strip().split())
            seedToSoil.append((src,dis,ran))
    with open(f"input{test}/soilToFert.txt", 'r') as file:
        for line in file: 
            dis, src, ran = map(int,line.strip().split())
            soilToFert.append((src,dis,ran))
    with open(f"input{test}/fertToWater.txt", 'r') as file:
        for line in file: 
            dis, src, ran = map(int, line.strip().split())
            fertToWater.append((src,dis,ran))
    with open(f"input{test}/waterToLight.txt", 'r') as file:
        for line in file: 
            dis, src, ran = map(int, line.strip().split())
            waterToLight.append((src,dis,ran))
    with open(f"input{test}/lightToTemp.txt", 'r') as file:
        for line in file: 
            dis, src, ran = map(int, line.strip().split())
            lightToTemp.append((src,dis,ran))
    with open(f"input{test}/tempToHumid.txt", 'r') as file:
        for line in file: 
            dis, src, ran = map(int, line.strip().split())
            tempToHumid.append((src,dis,ran))
    with open(f"input{test}/humidToLoca.txt", 'r') as file:
        for line in file: 
            dis, src, ran = map(int, line.strip().split())
            humidToLocation.append((src,dis,ran))

def isInRange(seed):
    #print(f"seed: {seed}")
    for i in seeds:
        start, ran = i
        #print(f"start: {start}, range: {ran}")
        if seed <= (start+ran) and seed >= start:
            return True
    return False

def searchReverse(item, lst):

    for ele in lst:
        src, dis, ran = ele
        max = (dis+ran)-1
        if item <= max and item >= dis:
            diff = item - dis
            return src + diff
    return item

def findReverse(loca, debug=False):
    if debug:print(f"loca: {loca}")
    humid = searchReverse(loca, humidToLocation)
    if debug:print(f"humid: {humid}")

    temp = searchReverse(humid, tempToHumid)
    if debug:print(f"temp: {temp}")

    light = searchReverse(temp, lightToTemp)
    if debug:print(f"light: {light}")

    water = searchReverse(light, waterToLight)
    if debug:print(f"water: {water}")

    fert = searchReverse(water, fertToWater)
    if debug:print(f"fert: {fert}")

    soil = searchReverse(fert, soilToFert)
    if debug:print(f"soil: {soil}")

    seed = searchReverse(soil, seedToSoil)
    if debug: print(f"seed: {seed}")

    return(isInRange(seed))

def readSeeds(s):
    lst = list()
    pairs = s.strip().split(",")
    for pair in pairs:
        a, b = pair.strip().split()
        lst.append((int(a),int(b)))
    return lst


read()

seeds = readSeeds(seedstr)

print(seeds)

found = False
i = 0

while(not found):
    print(f"location: {i}")
    found = findReverse(i)
    if found: 
        print(i)
    i += 1
