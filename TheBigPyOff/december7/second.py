from collections import Counter

def read(test=""):
    with open(f"input{test}/input.txt", 'r') as file: 
        d = dict()
        for line in file:
            card, bid = line.strip().split()
            d[card] = int(bid)
        return d

def findMostCommonNotJ(lst, debug=False):
    valuesToReturn = list()
    for l, c in lst: 
        if debug: print(l)
        if l != 'J': valuesToReturn.append(c)
    return valuesToReturn

def getCombi(numberOfJ, debug=False):
    match numberOfJ:
        case 1: return [(2,2), (1,3), (3,1)]
        case 2: return [(0,3), (3,0), (2,1), (1,2)]
        case 3: return [(2,0), (0,2), (1,1)]

def NoLettersExceptJ(card):
    return True if (("A" or "Q" or "K" or "T") not in card) else False
        

def FiveOfAKind(card, debug=False):
    c = Counter(card)
    thresh = 5 if "J" not in card else (5-card.count("J"))
    mostCommon = c.most_common(2)

    if(mostCommon[0][0] == "J" and mostCommon[0][1] == 5): return True

    jIsMostCommonAndNoBetterSolution = True if mostCommon[0][1] == "J" and NoLettersExceptJ(card) else False
    mostCommonNotJ = findMostCommonNotJ(c.most_common(2), debug)[0]
    if debug: print(f"FiveOfAKind threshhold: {thresh}, mostC: {mostCommon}")
    if (jIsMostCommonAndNoBetterSolution or mostCommonNotJ == thresh):
        return True
    else:
        return False

def FourOfAKind(card, debug=False):
    c = Counter(card)
    if debug: print(c)
    thresh = 4 if "J" not in card else (4-card.count("J"))
    
    mostCommon = findMostCommonNotJ(c.most_common(2), debug)[0]
    if (mostCommon == thresh):
        return True
    else:
        return False
    
def FullHouse(card, debug=False):
    c = Counter(card)
    if debug: print(c)
    mostCommon = findMostCommonNotJ(c.most_common(3), debug)
    combi = [(2,3),(3,2)] if "J" not in card else [(2,2)]
    count1 = mostCommon[0]
    count2 = mostCommon[1]
    for c1, c2 in combi:
        if ((count1 == c1 and count2 == c2)):
            return True
    return False
    
def ThreeOfAKind(card, debug=False):
    c = Counter(card)
    if debug: print(c)
    thresh = 3 if "J" not in card else (3-card.count("J"))
    mostCommon = findMostCommonNotJ(c.most_common(2), debug)[0]

    if (mostCommon == thresh):
        return True
    else:
        return False

def TwoPair(card, debug=False):
    #If contains J, it will always hit higher first
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
    #If contains J, it will always hit higher first
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
        if "J" in card: return 1
        else:
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



cards = read()

sortedCards = list()

debug = False

#print(getType("JJJJJ"))

for card in cards: 
    type = getType(card)
    sortedCards = addCard(card, type, sortedCards, debug)

if debug: print(sortedCards)
print(sortedCards)
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
#249776650
#250563394