# Advent of Code Day Five

import string

# Converts the values of an array of strings, or other values, to an integer list
# Parameter: list - array of decimal values currently formatted as other data type
def convertToIntList (list):
    for index in range(len(list)):
        list[index] = int(list[index])
    

def main():
    dataFile = open("DayFive.txt", 'r', encoding='UTF-8')

    currentValues = []
    
    seedLine = dataFile.readline().strip()

    seeds = seedLine[seedLine.index(":")+2:].split(" ")
    # print(seeds)

    convertToIntList(seeds)

    # print(seeds)

    # Part Two Segment

    # index = 0
    # finalSeedRange = []
    # while index < len(seeds):
    #     for i in range(seeds[index + 1]):
    #         finalSeedRange.append(seeds[index] + i)
    #     index += 2
    # seeds = finalSeedRange
    # print("Seeds Generated")

    # End Part Two Segment

    needToChange = seeds
    changed = []
    skipNext = True

    dataFile.readline()

    for line in dataFile:
        if not skipNext:
            lineData = line.strip()
            if len(lineData) == 0:
                needToChange = needToChange + changed
                changed = []
                skipNext = True
            else:
                values = lineData.split()
                convertToIntList(values)
                checkIndex = 0
                while checkIndex < len(needToChange):
                    difference = needToChange[checkIndex] - values[1]
                    if difference >= 0 and difference <= values[2]:
                        changed.append(difference + values[0])
                        needToChange.pop(checkIndex)
                    else:
                        checkIndex += 1
        else:
            skipNext = False
    finalValues = needToChange + changed
    # print(finalValues)

    print(min(finalValues))
    return

main()