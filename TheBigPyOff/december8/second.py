instructions = "LRRLRRRLRRRLLRRLRRLRLRLRRLLRRLRRLRRRLLLRRRLRRRLRRRLLRRRLRRLLRRLRRLRLRRRLRRLRLRRLRRRLLRRLLRLRRRLLRRLRRLLLRLRRRLRLRLRLLRRRLRLLRRRLRLRRRLRRRLLRRLRRRLLRRLRLLRLRRLLLRRLRRLLLRLLRLRRRLRLRLRRRLRRLLRRRLRLRLRRLRRRLRLRRLRRLRRRLRRRLRRRLRRRLRRLLRRLRLLRRLLRRRLRLLRLRLRRLRRLRLRLRRRLRLRLRRLRLRRLRRRR"
instructionsTest = "LR"
startingNodes = list()

map = dict()

lst = list()

def read(test=""):
    with open(f"input/{test}/input.txt", 'r') as file:
        for line in file: 
            key, values = line.strip().split("=")
            if key[2] == "A":
                startingNodes.append(key.strip())
            values = values.replace("(", " ").replace(")", " ")
            left, right = values.strip().split(",")
            map[key.strip()] = (left.strip(), right.strip())
    
def getNextNode(key, instruction):
    left, right = map.get(key)
    return left if instruction == "L" else right

def getLengthPaths():
    for node in startingNodes:
        i = 0
        max = len(instructions) - 1
        steps = 0
        while(node[2] != "Z"):
            instruct = instructions[i]
            node = getNextNode(node, instruct)
            i = i + 1 if i != max else 0
            steps += 1
        lst.append(steps)

def allModulo(i, test=False):
    if test:
        if  i % lst[0] == 0 and  i % lst[1] == 0 :
            return True
        else:
            return False
    else:
        if i % lst[0] == 0 and i % lst[1] == 0 and i % lst[2] == 0 and i % lst[3]== 0 and i % lst[4]== 0 and i % lst[5]== 0:
            return True
        else:
            return False

def cal(test=False):
    inc = max(lst)
    steps = inc
    while (not allModulo(steps, test)):
        steps += inc
    return steps

read()
print(startingNodes)

getLengthPaths()
print(lst)
print(cal())

