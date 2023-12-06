seedstr = "929142010 467769747 2497466808 210166838 3768123711 33216796 1609270159 86969850 199555506 378609832 1840685500 314009711 1740069852 36868255 2161129344 170490105 2869967743 265455365 3984276455 31190888"
seedstrTest = "79 14 55 13"

seedToSoil = list()
soilToFert = list()
fertToWater = list()
waterToLight = list()
lightToTemp = list()
tempToHumid = list()
humidToLocation = list()

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

def search(item, lst):
    for ele in lst:
        src, dis, ran = ele
        if item in range(src, src+ran):
            diff = item - src
            return dis + diff
    return item

def find(seed, debug=False):
    if debug: print(f"seed: {seed}")
    soil = search(seed, seedToSoil)

    if debug:print(f"soil: {soil}")
    fert = search(soil, soilToFert)
    
    if debug:print(f"fert: {fert}")
    water = search(fert, fertToWater)
    
    if debug:print(f"water: {water}")
    light = search(water, waterToLight)
    
    if debug:print(f"light: {light}")
    temp = search(light, lightToTemp)
    
    if debug:print(f"temp: {temp}")
    humid = search(temp, tempToHumid)
    
    if debug:print(f"humid: {humid}")
    loca = search(humid, humidToLocation)
    if debug:print(f"loca: {loca}")
    
    return loca

read()

seeds = map(int, seedstr.strip().split())
result = list()

for seed in seeds:
    result.append(find(seed))

result.sort()
print(result[0])


