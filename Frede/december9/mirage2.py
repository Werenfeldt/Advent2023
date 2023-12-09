
def algorithm(numberlist: list):
    diff_list = []
    for i in range(len(numberlist)):
        if not i == len(numberlist)-1:
            diff = int(numberlist[i+1]) - int(numberlist[i])
            diff_list.append(diff)

    if diff_list.count(0) != len(diff_list):
        new_list = algorithm(diff_list)
        numberlist.insert(0, int(numberlist[0]) - new_list[0])
        return numberlist
    else:
        diff_list.insert(0, 0)
        numberlist.insert(0, numberlist[0] - diff_list[0])
        return numberlist

totalSum = 0
with open('input.txt') as s:
    for line in s:
        linelist = line.strip().split(" ")
        result = algorithm(linelist)
        #print("result: ", result)
        totalSum += result[0]

print("totalSum: ", totalSum)
