import re
import math

def countWins(time, distance):
    return

def convertToIntList(list):
    for i in range(len(list)):
        list[i] = int(list[i])

def main():
    dataFile = open('DaySix.txt', 'r', encoding='UTF-8')
    timeLine = dataFile.readline().strip()
    distanceLine = dataFile.readline().strip()

    result = 1

    times = re.findall('\d+', timeLine)
    distances = re.findall('\d+', distanceLine)

    print(times)
    print(distances)

    partTwoTime = ""
    partTwoDistance = ""

    for i in range(len(times)):
        partTwoTime += times[i]
        partTwoDistance += distances[i]

    convertToIntList(times)
    convertToIntList(distances)

    # Part One:
    for i in range(len(times)):
        print("Set", i, ":")
        if times[i] >= distances[i]:
            result *= times[i] - 1 
        middleValue = math.ceil((times[i]-1) / 2) # Start Checking at middle
        print("\tMiddle Time:",middleValue)
        checkValue = middleValue
        done = False
        while checkValue >= 1 and done == False:
            print("\tCheck Value =", checkValue)
            distanceMoved = checkValue * (times[i] - checkValue)
            print("\tDistance Moved:", distanceMoved)
            if distanceMoved > distances[i]:
                checkValue -= 1
            else:
                done = True
        else:
            print(checkValue)
        matches = (middleValue - checkValue) * 2
        if (times[i] - 1) % 2 == 1:
            matches -= 1
        print("\t Matches",matches)
        result *= matches
    print("Part One Answer: " + str(result))


    # Part Two
    partTwoTime = int(partTwoTime)
    partTwoDistance = int(partTwoDistance)

    partTwoMiddle = math.ceil((partTwoTime - 1) / 2)
    twoCheckValue = partTwoMiddle
    twoDone = False

    while twoCheckValue >= 1 and not twoDone:
        distanceMoved = twoCheckValue * (partTwoTime - twoCheckValue)
        if distanceMoved > partTwoDistance:
            twoCheckValue -= 1
        else:
            twoDone = True
    matches = (partTwoMiddle - twoCheckValue) * 2
    if(partTwoTime - 1) % 2 == 1:
        matches -= 1
    print(matches)

main()