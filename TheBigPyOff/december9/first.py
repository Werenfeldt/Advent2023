lst = list()

def read(test=""):
    with open(f"input{test}/input.txt", 'r') as file:
        for line in file: 
            numbers = list(map(int, line.split()))
            lst.append(numbers)

def predict(numbers, debug=False):
    diffLst = list()
    for i, number in enumerate(numbers, 1):
        if debug: 
            print(f"number: {number}")
            print(f"prev number: {numbers[i]}")
        diff = numbers[i] - number  
        if debug: print(f"diff: {diff}")
        diffLst.append(diff)
        if(i == len(numbers)-1): break
    if debug: 
        print(f"first diff: {diffLst[0]}")
        print(f"len of diff: {len(diffLst)}")
        allSame = diffLst.count(diffLst[0]) == len(diffLst)
        print(f"all same diff?: {allSame}")

    if diffLst.count(diffLst[0]) == len(diffLst):
        return numbers[-1] + diffLst[0]
    else: 
        return numbers[-1] + predict(diffLst, debug)

def run(debug=False):
    sum = 0
    for line in lst: 
        n = predict(line, debug)
        if debug: print(f"returned: {n}")
        sum += n
    return sum

debug = False
read()
#print(lst)
result = run(debug)
print(result)


