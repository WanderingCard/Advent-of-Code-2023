# Advent of Code Day Five, Part 2
import re

# Converts the values of an array of strings, or other values, to an integer list
# Parameter: list - array of decimal values currently formatted as other data type
def convertToIntList (list):
    for index in range(len(list)):
        list[index] = int(list[index])

def sortListofList(list, sortIndex):
    smallestIndex = 0
    for i in range(len(list)-1):
        smallestIndex = i
        index = i + 1
        while index < len(list):
            if list[index][sortIndex] < list[smallestIndex][sortIndex]:
                smallestIndex = index
            index += 1
        temp = list[i]
        list[i] = list[smallestIndex]
        list[smallestIndex] = temp

def main():
    dataFile = open('DayFive.txt', 'r', encoding='UTF-8')

    seedRanges = [] # Stores sets of ranges in form (start, end)

    seedLine = dataFile.readline().strip()
    numbers = re.findall('\d+', seedLine)
    print(numbers)

    index = 0
    while index < len(numbers):
        rangePair = [int(numbers[index]), int(numbers[index]) + int(numbers[index+1])]
        index += 2
        seedRanges.append(rangePair)

    # Gather Each Sections' Pairs
    
    dataRanges = [] # List of Lists of Integers, Index 1 - Section (Seed to Soil, etc.), 2 - Which range from the section, 3 - Which Value in the range (1 - Source Start, 2 - Source End, 3 - Dest Start, 4 - Dest End)
    section = 0

    skipNext = True

    dataFile.readline()

    sectionRanges = []

    for line in dataFile:
        if not skipNext:
            lineData = line.strip()
            if len(lineData) == 0:
                dataRanges.append(sectionRanges)
                sectionRanges = []
                skipNext = True
            else:
                values = lineData.split()
                convertToIntList(values)
                print(values)
                newRange = [values[1], values[1] + values[2]-1, values[0], values[0] + values[2]]
                print(newRange)
                print("\n")
                sectionRanges.append(newRange)
        else:
            skipNext = False
    dataRanges.append(sectionRanges)
    
    sortListofList(seedRanges, 0)
    print (seedRanges)
    index = 1
    for i in dataRanges:
        print("Section " + str(index) + ":\n\n")
        sortListofList(i, 0)
        for j in i:
            print(j)
        print("\n")
        index += 1

    valueRanges = seedRanges

    conversionRound = 1

    for i in dataRanges:
        modifiedRanges = list.copy(valueRanges)
        finishedRanges = []

        valueIndex = 0
        modifIndex = 0
        print(i)

        while valueIndex < len(i) and modifIndex < len(modifiedRanges):
            # Check if modifiedRange endValue > conversionRange endValue - Create Finished Range from modifiedStart to endRange of conversion source
            print("Checking the range from {} to {} against the range {} to {}".format(modifiedRanges[modifIndex][0], modifiedRanges[modifIndex][1], i[valueIndex][0], i[valueIndex][1]))
            if modifiedRanges[modifIndex][0] < i[valueIndex][0]:
                if modifiedRanges[modifIndex][1] < i[valueIndex][0]:
                    finishedRanges.append(modifiedRanges[modifIndex])
                    modifIndex += 1
                else:
                    finishedRanges.append([modifiedRanges[modifIndex][0], i[valueIndex][0]])
                    modifiedRanges[modifIndex][0] = i[valueIndex][0] 
            elif modifiedRanges[modifIndex][0] > i[valueIndex][1]:
                valueIndex += 1
                if valueIndex >= len(i):
                    while modifIndex < len(modifiedRanges):
                        finishedRanges.append(modifiedRanges[modifIndex])
                        modifIndex += 1
            else:
                # If the prechanged range's end value is higher than the end value of the conversion table index
                if modifiedRanges[modifIndex][1] >= i[valueIndex][1]:
                    # Calculate Start Value of Converted Range
                    startGap = modifiedRanges[modifIndex][0] - i[valueIndex][0]
                    startConvertValue = i[valueIndex][2] + startGap
                    finishedRanges.append([startConvertValue, i[valueIndex][3]])    # Add the coverted range starting with 
                    modifiedRanges[modifIndex][0] = i[valueIndex][1]+1
                    valueIndex += 1
                    if valueIndex >= len(i):
                        while modifIndex < len(modifiedRanges):
                            finishedRanges.append(modifiedRanges[modifIndex])
                            modifIndex += 1
                elif modifiedRanges[modifIndex][1] < i[valueIndex][1]:
                    startGap = modifiedRanges[modifIndex][0] - i[valueIndex][0]
                    endGap = modifiedRanges[modifIndex][1] - i[valueIndex][0]
                    startConvertValue = i[valueIndex][2] + startGap
                    endConvertValue = i[valueIndex][2] + endGap
                    finishedRanges.append([startConvertValue, endConvertValue+1])
                    modifiedRanges.pop(modifIndex)
        if modifIndex > len(modifiedRanges):
            valueRanges = finishedRanges + modifiedRanges
        else:
            valueRanges = finishedRanges
        print("========== Conversion Round", conversionRound, "==========")
        print(valueRanges)
        sortListofList(valueRanges, 0)
        conversionRound += 1
    print(valueRanges[0])


main()