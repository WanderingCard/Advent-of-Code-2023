# Advent of Code Day One Code. 

import re

def main():
    sum = 0
    numRegExp = '\d'
    # Look ahead ?= Allows for non consumption of values, fixes twone issue.
    partTwoRegExp = '(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))'
    valueConvert = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    textPattern = re.compile(partTwoRegExp)
    dataFile = open('DayOne.txt', 'r', encoding='utf-8')
    lineCount = 1

    for line in dataFile:
        # print(lineCount, line)
        lineTotal = 0
        
        lineConcat = ''

        # Part One 
        # numbers = re.findall(numRegExp, line)
        # lineConcat = numbers[0] + numbers[len(numbers)-1]
        # print(lineConcat)

        # Part Two
        numbers = re.findall(textPattern, line)
        if numbers[0] in valueConvert:
            lineConcat = str(valueConvert.index(numbers[0])+1)
        else:
            lineConcat = numbers[0]

        if numbers[len(numbers)-1] in valueConvert:
            lineConcat += str(valueConvert.index(numbers[len(numbers)-1])+1)
        else:
            lineConcat += numbers[len(numbers)-1]

        print(lineCount, lineConcat, numbers)

        lineTotal = int(lineConcat)
        sum += lineTotal
        lineCount += 1
    print("Sum: ", sum)
    
    return
main()