# Advent of Code Day Two Code

import re

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

        # Part One
        if minReds <= 12 and minGreens <= 13 and minBlues <= 14:
            validRounds.append(roundCount+1)
        roundCount += 1

        # Part Two
        roundTotal = minBlues * minReds * minGreens
        partTwoSum += roundTotal
        # print(roundTotal)
        # print(str(partTwoSum) + "\n")
    print(str(sum(validRounds)))
    print(str(partTwoSum))

main()