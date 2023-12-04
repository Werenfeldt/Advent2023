cards = list()
sum = 0

def getWinningNum(n):
    num = n.split(':')[1]
    num.strip()
    numInts = list(map(int, num.split()))
    return numInts

def getMyNum(n):
    n.strip()
    numInts = list(map(int, n.split()))
    return numInts

with open("input/input.txt", 'r') as file:
    for line in file:
        cardSum = 0
        first = True
        winningNumbers, myNumbers = line.split('|')
        winningNumbersList = getWinningNum(winningNumbers)
        myNumbersList = getMyNum(myNumbers)
        #print(winningNumbersList)
        #print(myNumbersList)
        for n in winningNumbersList:
            #print(n)
            if (n in myNumbersList):
                if(first):
                    cardSum += 1
                    first = False
                else:
                    cardSum += cardSum
        #print(cardSum)
        sum += cardSum
print(sum)