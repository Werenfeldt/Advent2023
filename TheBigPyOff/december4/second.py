cards = list()
numOfCards = [1 for i in range(189)]
#numOfCards = [1 for i in range(6)]
totalCards = 1

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

    for id, line in enumerate(file):
        winningNums = 0
        winningNumbers, myNumbers = line.split('|')
        winningNumbersList = getWinningNum(winningNumbers)
        myNumbersList = getMyNum(myNumbers)
        #print(winningNumbersList)
        #print(myNumbersList)
        for n in winningNumbersList:
            #print(n)
            if (n in myNumbersList):
                winningNums += 1
        #print(f"in card index {id}, there is {winningNums} winning numbers")
        numberOfCards = numOfCards[id]
        for n in range(winningNums):
            numOfCards[id+n+1] += numberOfCards

print(sum(numOfCards))
