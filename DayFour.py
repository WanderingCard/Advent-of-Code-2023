# Advent of Code Day 4

import re

def main():
    dataFile = open('DayFour.txt', 'r', encoding='utf-8')
    pointsTotal = 0
    totalGames = 0
    futureCopies = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for line in dataFile:
        cardRepeats = futureCopies[0]+1
        for i in range(len(futureCopies)-1):
            futureCopies[i] = futureCopies[i+1]
        futureCopies[9] = 0

        matches = 0
        winningNumbers = []
        removeLabel = line[line.find(': ')+1:]
        winningNumbers = re.findall('\d+', removeLabel[:removeLabel.find('|')])
        myNumbers = re.findall('\d+', removeLabel[removeLabel.find('|'):])

        for number in myNumbers:
            if number in winningNumbers:
                matches += 1
        
        for i in range(matches):
            futureCopies[i] += cardRepeats

        gameTotal = pow(2, matches-1) if matches > 0 else 0

        pointsTotal += gameTotal

        totalGames += cardRepeats

        # print(winningNumbers)
        # print(myNumbers, '\n', roundPoints, '\n')
    print(pointsTotal)
    print(totalGames)

main()