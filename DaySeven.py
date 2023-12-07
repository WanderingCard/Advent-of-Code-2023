# Advent of Code Day 7

def checkHandClass(hand, jokers):
    if not jokers:
        return noJokersClass(hand)
    return jokersClass(hand)

# Must always be at least one joker
def jokersClass(hand: str):
    jokersCount = hand.count('J')
    nonJokers = list(filter(None, hand.split('J'))) # Get a list of non joker cards
    
    # All Card Combos Need to involve a Joker, so no naturals of any hands should be possible. 

    # Five of a kind: Count first non joker value + jokers == 5 or Five Jokers

    jokerString = ""
    for i in nonJokers:
        jokerString += i

    nonJokers = jokerString

    if jokersCount == 5:
        return 1

    if nonJokers.count(nonJokers[0]) + jokersCount == 5:
        return 1
    
    presentCards = []
    cardCount = []

    for card in nonJokers:
        if card in presentCards:
            cardCount[presentCards.index(card)] += 1
        else:
            presentCards.append(card)
            cardCount.append(1)
    
    print(hand, cardCount)
    print(presentCards, cardCount)

    # Four of a kind: Count a card value + jokers == 4 - Value 2
    if max(cardCount) + jokersCount == 4:
        return 2

    # Full House: Need either Two pairs, or a Three of A Kind - Value 3
    if 3 in cardCount:
        return 3
    if cardCount.count(2) == 2:
        return 3

    # Three of a Kind: Need a pair or nat Three of a Kind - Value 4
    if 2 in cardCount:
        return 4

    # All cards only have 1 of itself.
    if jokersCount == 2:
        return 4
    return 6


def noJokersClass(hand):
    if hand.count(hand[0]) == 5:
        return 1
    pairs = []
    foundThreeOfAKind = False

    for card in hand:
        if hand.count(card) == 4:
            return 2
        if hand.count(card) == 3:
            foundThreeOfAKind = True
        if hand.count(card) == 2:
            if card not in pairs:
                pairs.append(card)
        if foundThreeOfAKind and len(pairs) > 0:
            return 3
    if foundThreeOfAKind:
        return 4
    if len(pairs) == 2:
        return 5
    if len(pairs) == 1:
        return 6
    return 7

def sortHandList(handList, sortIndex, jokersOn):
    if len(handList) <= 1:
        return handList
    
    if not jokersOn:
        characterOrder = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    else:
        characterOrder = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    sortArray = [[], [], [], [], [], [], [], [], [], [], [], [], []]

    for hand in handList:
        sortCard = hand[0][sortIndex]
        sortArray[characterOrder.index(sortCard)].append(hand)
    
    output = []

    # At this point the whole array is now subdivided by the card at index sortIndex..
    # If this is the last index, we want to return the sorted list in card order as an array..

    if sortIndex == 4:
        for set in sortArray:
            output = output + set
        return output

    # Else we want to sort each grouping by the next index

    for set in sortArray:
        output = output + sortHandList(set, sortIndex + 1, jokersOn)
    
    return output
    # Then we want to merge them

def main():
    dataFile = open("DaySeven.txt", 'r', encoding='UTF-8')

    cardClasses = [[], [], [], [], [], [], []]  # 2D Array storing the cards sorted by hand value, index 1 - hand class (out-1), 2 the specific hand, 3 the bid ammount of a hand 

    classList = ["Five of a Kind", "Four of a Kind", "Full House", "Three of a Kind", "Two Pair", "One Pair", "High Card"]

    totalHands = 0
    totalScore = 0

    for line in dataFile:
        data = line.strip().split(" ")
        # Part One
        # handClass = checkHandClass(data[0], False) - 1

        # Part Two
        handClass = checkHandClass(data[0], 'J' in data[0]) - 1

        cardClasses[handClass].append(data)
        totalHands += 1

        # print(data)
        # print(cardClasses[handClass], "\n")

    # print()

    # for i in range(len(cardClasses)):
    #     print("Hand Class", classList[i])
    #     print("\t", cardClasses[i])

    print("Sorted Hand Lists: ")

    nextRank = totalHands

    for i in range(len(cardClasses)):
        print("Hand Class", classList[i])
        # Part One
        # cardClasses[i] = sortHandList(cardClasses[i], 0, False)
        
        # Part Two
        cardClasses[i] = sortHandList(cardClasses[i], 0, True)
        print("\t", cardClasses[i])
        for hand in cardClasses[i]:
            totalScore += nextRank * int(hand[1])
            nextRank -= 1

    print("Final Result:", totalScore)
    return

main()