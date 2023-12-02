# Advent of Code Day Two Code

import re


colors = ['red', 'green', 'blue']
colorMax = [12, 13, 14]

def sumTo(val):
    total = 0
    for i in range(val):
        total += i+1
    return total

def checkGame(gameString):
    rounds = re.split('; ', gameString)
    for round in rounds:
        if checkRound(round) == False:
            return False
    return True

def checkRound(roundString):
    cubeSets = re.split(', ', roundString)
    for colorSet in cubeSets:
        divideColor = re.split(' ', colorSet)
        if colorValid(divideColor[1], divideColor[0]) == False:
            return False
    return True

def colorValid(color, count):
    maxValid = colorMax[colors.index(color)]
    if int(count) > maxValid:
        return False
    return True

def convertToIntArray(array):
    output = []
    for item in array:
        convert = int(item)
        output.append(convert)
    return output

def main():
    validRounds = []
    roundCount = 0
    partTwoSum = 0

    dataFile = open('DayTwo.txt', 'r', encoding='utf-8')
    for line in dataFile:
        lineData = re.split(': |\n',line)
        lineString = lineData[1]
        # Part One
        # if checkGame(lineString):
        #    validRounds.append(roundCount)
        # else:
        #    print(line)
        # roundCount += 1 
    # print(validRounds)
    # print("Sum: " + str(sum(validRounds)))

        # Part Two
        blueExp = '(\d+) blue'
        redExp = '(\d+) red'
        greenExp = '(\d+) green'

        blueValues = convertToIntArray(re.findall(blueExp, lineString))
        # print(blueValues)
        redValues = convertToIntArray(re.findall(redExp, lineString))
        # print(redValues)
        greenValues = convertToIntArray(re.findall(greenExp, lineString))
        # print(greenValues)

        minBlues = int(max(blueValues))
        # print("Min Blues: ", minBlues)
        minReds = int(max(redValues))
        # print("Min Reds: ", minReds)
        minGreens = int(max(greenValues))
        # print("Min Greens: ", minGreens)

        roundTotal = minBlues * minReds * minGreens
        # print(roundTotal)
        partTwoSum += roundTotal
        # print(str(partTwoSum) + "\n")
    print(str(partTwoSum))

    # Preliminary Part Two Testing
    # gameOne = "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    # blueExp = '(\d)+ blue'
    # redExp = '(\d)+ red'
    # greenExp = '(\d)+ green'
    # blueValues = re.findall(blueExp, gameOne)
    # redValues = re.findall(redExp, gameOne)
    # greenValues = re.findall(greenExp, gameOne)
    # print(blueValues)
    # print(redValues)
    # print(greenValues)
    # print("Max Blues:", str(max(blueValues)))

main()