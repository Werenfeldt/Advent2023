time = list()
dis = list()

def read(test=''):

    with open(f"input/{test}/time.txt", 'r') as file:
        for line in file:
            t = list(map(int, line.strip().split()))
            time.extend(t)
    with open(f"input/{test}/dis.txt", 'r') as file:
        for line in file:
            d = list(map(int, line.strip().split()))
            dis.extend(d)

read("")

def getRounds(n):
    if n % 2 == 0:
        return int((n/2))
    else:
        return int((n-1)/2)

def calDis(i, t):
    return i * (t-i)

def calWinningAmount(time, lastRecord):
    winning = 0
    rounds = getRounds(time)
    while (rounds > 0):
        result = calDis(rounds, time)
        #print(result)
        if(result > lastRecord):
            winning += 1
            rounds -= 1
        else:
            rounds = 0
    #print(winning)
    if time % 2 == 0:
        return (winning * 2) - 1
    else: 
        return winning * 2

print(time)
print(dis)

#part 1
print("Part 1")
mul = 1

for n in range(len(time)): 
    t = time[n]
    d = dis[n]
    result = calWinningAmount(t, d)
    #print(result)
    mul *= result

print(mul)

print("Part 2")

print(calWinningAmount(40709879, 215105121471005))