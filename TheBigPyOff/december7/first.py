from collections import Counter

def read(test=""):
    with open(f"input{test}/input.txt", 'r') as file: 
        d = dict()
        for line in file:
            card, bid = line.strip().split()
            d[card] = int(bid)
        return d

def FiveOfAKind(card, debug=False):
    c = Counter(card)
    if debug: print(f"c")
    mostCommon = c.most_common(1)[0][1]
    if (mostCommon == 5):
        return True
    else:
        return False

def FourOfAKind(card, debug=False):
    c = Counter(card)
    if debug: print(c)
    mostCommon = c.most_common(1)[0][1]
    if (mostCommon == 4):
        return True
    else:
        return False
    
def FullHouse(card, debug=False):
    c = Counter(card)
    if debug: print(c)
    mostCommon = c.most_common(2)
    combi = [(2,3),(3,2)]
    count1 = mostCommon[0][1]
    count2 = mostCommon[1][1]
    for c1, c2 in combi:
        if ((count1 == c1 and count2 == c2)):
            return True
        else:
            return False
    
def ThreeOfAKind(card, debug=False):
    c = Counter(card)
    if debug: print(c)
    mostCommon = c.most_common(1)[0][1]
    if (mostCommon == 3):
        return True
    else:
        return False

def TwoPair(card, debug=False):
    c = Counter(card)
    if debug: print(c)
    pairs = c.most_common(2)
    count1 = pairs[0][1]
    count2 = pairs[1][1]
    if count1 == 2 and count2 == 2:
        return True
    else: 
        return False
        
def OnePair(card, debug=False):
    c = Counter(card)
    if debug: print(c)
    pairs = c.most_common(2)
    count1 = pairs[0][1]
    count2 = pairs[1][1]
    if count1 == 2 and count2 != 2:
        return True
    else: 
        return False
        
def HighCard(card, debug=False):
    c = Counter(card)
    if debug: print(c)
    count = c.most_common()
    if(len(count)==5):
        return True
    else: 
        return False

def getType(card):
    if(FiveOfAKind(card)):
        return 6
    elif(FourOfAKind(card)):
        return 5
    elif(FullHouse(card)):
        return 4
    elif(ThreeOfAKind(card)):
        return 3
    elif(TwoPair(card)):
        return 2
    elif(OnePair(card)):
        return 1
    elif(HighCard(card)):
        return 0

def isCardHigher(c1, c2, debug=False):

    for i in range(len(c1)):
        p1 = c1[i]
        p2 = c2[i]
        if debug: print(f"p1: {p1}, p2: {p2}")
        if(p1 == p2): 
            if debug: print("continuing")
            continue
        if(p1.isdigit() and p2.isdigit()):
            if debug: print(f"two digits: returning: {p1 > p2}")
            return True if p1 > p2 else False
        elif(p1.isdigit() and not p2.isdigit()):
            if debug: print(f"p1 is digit and p2 is not:")
            return True if p2 == "J" else False
            
        elif(p2.isdigit() and not p1.isdigit()):
            if debug: print(f"p2 is digit and p1 is not:")
            return False if p1 == "J" else True
        else:
            match p1:
                case "A":
                    if debug: print(f"returning case 1") 
                    return True
                case "J": 
                    if debug: print(f"returning case 2") 
                    return False
                case "T" : 
                    if debug: print(f"returning case 3") 
                    return True if p2 == "J" else False
                case "Q": 
                    if debug: print(f"returning case 4") 
                    return True if p2 == "T" or p2 == "J" else False
                case "K":
                    if debug: print(f"returning case 5") 
                    return False if p2 == "A" else True

                
def addCard(cardToAdd, typeToAdd, lst, debug=False):
    newCards = list()
    if debug: print(f"----------------")
    if debug: print(f"adding card{(cardToAdd, typeToAdd)}")
    if debug: print(f"startting list: {lst}")
    for i, card in enumerate(lst):
        c, type = card
        if debug: print(f"i: {i}, card: {c}, type: {type}")

        if typeToAdd > type:
            if debug: print(f"type to add over adding card{(cardToAdd, typeToAdd)}")
            newCards.append((cardToAdd, typeToAdd))
            if debug: print(f"rest of list {lst[i:]}")
            newCards.extend(lst[i:])
            return newCards
        elif typeToAdd == type:
            if debug: print(f"same type")
            higher = isCardHigher(cardToAdd, c, debug)
            if debug: print(f"is card to add higher?: {higher}")
            if(isCardHigher(cardToAdd, c, debug)):
                if debug: print(f"first add: {cardToAdd, typeToAdd}  then: {c, type}")
                newCards.append((cardToAdd, typeToAdd))
                newCards.append((c, type))
                if debug: print(f"rest of list {lst[i+1:]}")
                newCards.extend(lst[i+1:])
                if debug: print(f"returning: {newCards}")
                return newCards
            else:
                if debug: print(f"first add: {c, type} then: {cardToAdd, typeToAdd}")
                newCards.append((c, type))

        else:
            if debug: print(f"ELSE adding: {c, type}")
            newCards.append((c,type))

        
    

    newCards.append((cardToAdd, typeToAdd))

    if debug: print(f"returning: {newCards}")
    return newCards



cards = read("/test")

sortedCards = list()

debug = True


for card in cards: 
    type = getType(card)
    sortedCards = addCard(card, type, sortedCards, debug)

if debug: print(sortedCards)
#print(cards)
i = len(sortedCards)
#print(i)
result = 0
for card in sortedCards:
    c = card[0]
    bid = cards.get(c)

    result += (bid*i)
    i -= 1

print(result)

#249676572
#249939488
#249979530
#249638405