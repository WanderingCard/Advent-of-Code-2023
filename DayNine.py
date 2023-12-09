# Advent of Code Day 9

def convertToIntList(list):
    for i in range(len(list)):
        list[i] = int(list[i])
    return list

def getDifferences(line: list) -> list:
    output = [line]
    currentLineOut = line

    while currentLineOut.count(0) != len(currentLineOut):
        newLineOut = []
        for i in range(len(currentLineOut) - 1):
            newLineOut.append(currentLineOut[i+1] - currentLineOut[i])
        output.append(newLineOut)
        currentLineOut = newLineOut
    
    return output


def predictNext(differences:list[list]) -> int:
    checkIndex = len(differences) - 1
    predictValue = 0
    while checkIndex > 0:
        predictValue = differences[checkIndex - 1][-1] + predictValue
        checkIndex -= 1
    return predictValue

def predictPast(differences:list[list]) -> int:
    checkIndex = len(differences) - 1
    predictValue = 0
    while checkIndex > 0:
        predictValue = differences[checkIndex - 1][0] - predictValue
        checkIndex -= 1
    return predictValue

def main():
    dataFile = open('DayNine.txt', 'r', encoding='UTF-8')

    partOneTotal = 0
    partTwoTotal = 0

    for line in dataFile:
        data = convertToIntList(line.strip().split())
        differences = getDifferences(data)
        print(differences)
        prediction = predictNext(differences)
        print("Next Value:", prediction)
        partOneTotal += prediction
        partTwoTotal += predictPast(differences)

    print("Part One:", partOneTotal)
    print("Part Two:", partTwoTotal)
    dataFile.close()
    return

main()