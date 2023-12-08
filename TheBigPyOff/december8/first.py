instructions = "LRRLRRRLRRRLLRRLRRLRLRLRRLLRRLRRLRRRLLLRRRLRRRLRRRLLRRRLRRLLRRLRRLRLRRRLRRLRLRRLRRRLLRRLLRLRRRLLRRLRRLLLRLRRRLRLRLRLLRRRLRLLRRRLRLRRRLRRRLLRRLRRRLLRRLRLLRLRRLLLRRLRRLLLRLLRLRRRLRLRLRRRLRRLLRRRLRLRLRRLRRRLRLRRLRRLRRRLRRRLRRRLRRRLRRLLRRLRLLRRLLRRRLRLLRLRLRRLRRLRLRLRRRLRLRLRRLRLRRLRRRR"

startingNodes = list()

map = dict()

def read(test=""):
    with open(f"input/{test}/input.txt", 'r') as file:
        for line in file: 
            key, values = line.strip().split("=")
            values = values.replace("(", " ").replace(")", " ")
            left, right = values.strip().split(",")
            map[key.strip()] = (left.strip(), right.strip())
    

def getNextNode(key, instruction):
    left, right = map.get(key)
    return left if instruction == "L" else right


def run():
    i = 0
    max = len(instructions) - 1
    steps = 0
    node = "AAA"
    while(node != "ZZZ"):
        instruct = instructions[i]
        node = getNextNode(node, instruct)
        i = i + 1 if i != max else 0
        steps += 1
    return steps


read()

result = run()
print(result)

