
def algorithm(numberlist: list):
    diff_list = []
    for i in range(len(numberlist)):
        if not i == len(numberlist)-1:
            diff = int(numberlist[i+1]) - int(numberlist[i])
            diff_list.append(diff)

    if diff_list.count(0) != len(diff_list):
        new_list = algorithm(diff_list)
        numberlist.append(int(numberlist[-1]) + new_list[-1])
        return numberlist
    else:
        diff_list.append(0)
        numberlist.append(numberlist[len(numberlist)-1] + diff_list[len(diff_list)-1])
        return numberlist

totalSum = 0
with open('input.txt') as s:
    for line in s:
        linelist = line.strip().split(" ")
        result = algorithm(linelist)
        #print("result: ", result)
        totalSum += result[-1]

print("totalSum: ", totalSum)
