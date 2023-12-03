def getNumber(line, index) -> list[int]:
    start = findStart(line, index-1)
    end = findEnd(line, index+1)
    value = int(line[start:end+1])
    output = [start, end, value]
    return output

def findStart(line:str, index:int) -> int:
    if index < 0 or line[index].isnumeric() == False:
        return index+1
    return findStart(line, index-1)

def findEnd(line, index) -> int:
    if index >= len(line) or line[index].isnumeric() == False:
        return index-1
    return findEnd(line, index+1)

def generateString(character, times):
    output = ''
    for x in range(times):
        output += character
    return output

def checkGear(lines, gearRow, gearCol):
    return (len(getAdjacentValues(lines, gearRow, gearCol)) == 2)

def getGearRatio(lines, gearRow, gearCol):
    gearValues = getAdjacentValues(lines, gearRow, gearCol)
    return gearValues[0] * gearValues[1]

def getAdjacentValues(lines, centerRow, centerCol, replace):
    output = []
    checkRow = centerRow - 1 if centerRow > 0 else centerRow
    while checkRow < min(len(lines), centerRow + 2):
        checkCol = centerCol - 1 if centerCol > 0 else centerCol
        rowString = lines[checkRow]
        while checkCol < min(len(rowString), centerCol + 2):
            if rowString[checkCol].isnumeric():
                numData = getNumber(rowString, checkCol)
                output.append(numData[2])
                if replace:
                    periodString = generateString('.', numData[1] - numData[0] + 1)
                    removeLine = lines[checkRow][:numData[0]] + periodString + lines[checkRow][numData[1]+1:]
                    lines[checkRow] = removeLine
                checkCol = numData[1]+1
            else:
                checkCol += 1
        checkRow += 1
    return output


def main():
    dataFile = open('DayThree.txt', 'r', encoding='utf-8')

    lines = [] # Stores all the lines as strings

    numberStart = [] # Might help find location of the start of numbers
    numberEnds = [] # Stores end index of numbers in lines

    for line in dataFile:
        if len(lines) == 0:
            lines.append(line[:len(line)-1])
        else:
            lines.append(line[:len(lines[0])]) # Store Lines in an Array and excluding the new line if present
    
    # print(lines[4])

    # print(len(lines))

    # print(len(lines[0]))

    # print(lines[0][139])
    partNumbers = []

    for lineNum in range(len(lines)):
        lastChar = '.'
        lineStarts = []
        lineEnds = []
        testLine = lines[lineNum]
        index = 0
        while index < len(testLine):
            if testLine[index].isnumeric() == False and testLine[index] != '.':
                # Symbol Found, do Things with it

                print("Symbol Found in line", lineNum, "index:", index)

                checkRow = lineNum - 1 if lineNum > 0 else lineNum
                while checkRow <= min(len(lines), lineNum + 1):
                    checkCol = index - 1 if index > 0 else index
                    while checkCol <= min(len(testLine), index + 1):
                        if lines[checkRow][checkCol].isnumeric():

                            print("\tNumber found in line", checkRow, "at spot", checkCol)

                            # Get Number and Info
                            outputData = getNumber(lines[checkRow], checkCol)
                            startIndex = outputData[0]
                            endIndex = outputData[1]
                            value = outputData[2]

                            # Remove Value from String
                            periodString = generateString('.', endIndex - startIndex + 1)
                            removeLine = lines[checkRow][:startIndex] + periodString + lines[checkRow][endIndex+1:]
                            lines[checkRow] = removeLine

                            # Add Value to Part List
                            partNumbers.append(value)

                            # Change CheckRow to end Value
                            checkCol = endIndex + 1
                        else:
                            checkCol += 1
                    checkRow += 1
            index += 1
    print(partNumbers)
    print(sum(partNumbers))

    dataFile.close()

    return 

main()