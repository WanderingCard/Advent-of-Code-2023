# Advent of Code Day Ten

import re

def printArray(list):
    for i in list:
        print(i)

def canMoveUp(map, row, col):
    validSymbols = ['|', '7', 'F', 'S']
    if row > 0 and map[row-1][col] in validSymbols:
        return True
    return False

def canMoveRight(map, row, col):
    validSymbols = ['-', 'J', '7', 'S']
    if col < len(map[0])-1 and map[row][col+1] in validSymbols:
        return True
    return False

def canMoveDown(map, row, col):
    validSymbols = ['|', 'L', 'J', 'S']
    if row < len(map) - 1 and map[row+1][col] in validSymbols:
        return True
    return False

def canMoveLeft(map, row, col):
    validSymbols = ['-', 'L', 'F', 'S']
    if col > 0 and map[row][col-1] in validSymbols:
        return True
    return False

def countMoves(map, row, col, markLoop):
    moveUpSymbols = ['|', 'L', 'J']
    moveLeftSymbols = ['-', 'J', '7']
    moveRightSymbols = ['-', 'L', 'F']
    moveDownSymbols = ['|', '7', 'F']

    moves = 0
    currentRow = row
    currentCol = col
    lastDirection = 'NA'

    markedMap = []
    for line in map:
        copyRow = line.copy()
        markedMap.append(copyRow)

    while map[currentRow][currentCol] != 'S' or lastDirection == 'NA':
        if map[currentRow][currentCol] == 'S':
            if canMoveUp(map, row, col):
                currentRow -= 1
                lastDirection = 'U'
                # print("Move", moves, "Up from", currentRow+1, currentCol, "to", currentRow, currentCol)
                moves += 1
                # return countMoves(map, row-1, col, 'U')
            elif canMoveRight(map, row, col):
                currentCol += 1
                lastDirection = 'R'
                # print("Move", moves, "Right from", currentRow, currentCol-1, "to", currentRow, currentCol)
                moves += 1
                # return countMoves(map, row, col+1, 'R')
            elif canMoveDown(map, row, col):
                currentRow += 1
                lastDirection = 'D'
                # print("Move", moves, "Down from", currentRow-1, currentCol, "to", currentRow, currentCol)
                moves += 1
                # return countMoves(map, row+1, col, 'D')
            elif canMoveLeft(map, row, col):
                currentCol -= 1
                lastDirection = 'L'
                # print("Move", moves, "Left from", currentRow, currentCol+1, "to", currentRow, currentCol)
                moves += 1
                # return countMoves(map, row, col-1, 'L')
        else:
            if lastDirection != 'D' and map[currentRow][currentCol] in moveUpSymbols:
                currentRow -= 1
                lastDirection = 'U'
                # print("Move", moves, "Up from", currentRow+1, currentCol, "to", currentRow, currentCol)
                moves += 1
                # return 1 + countMoves(map, row-1, col, 'U')
            elif lastDirection != 'L' and map[currentRow][currentCol] in moveRightSymbols:
                currentCol += 1
                lastDirection = 'R'
                # print("Move", moves, "Right from", currentRow, currentCol-1, "to", currentRow, currentCol)
                moves += 1
                # return 1 + countMoves(map, row, col+1, 'R')
            elif lastDirection != 'U' and map[currentRow][currentCol] in moveDownSymbols:
                currentRow += 1
                lastDirection = 'D'
                # print("Move", moves, "Down from", currentRow-1, currentCol, "to", currentRow, currentCol)
                moves += 1
                # return 1 + countMoves(map, row+1, col, 'D')
            elif lastDirection != 'R' and map[currentRow][currentCol] in moveLeftSymbols:
                currentCol -= 1
                lastDirection = 'L'
                # print("Move", moves, "Left from", currentRow, currentCol+1, "to", currentRow, currentCol)
                moves += 1
                # return 1 + countMoves(map, row, col-1, 'L')
        markedMap[currentRow][currentCol] = 'O'
    if markLoop:
        return [moves, markedMap]
    return moves

def main():
    # Do Something

    dataFile = open('DayTen.txt', 'r', encoding='UTF-8')
    startRow = -1
    startCol = -1
    moveArray = []
    for line in dataFile:
        lineData = re.findall(".{1}", line)
        if 'S' in lineData:
            startRow = len(moveArray)
            startCol = lineData.index('S')
        moveArray.append(lineData)
    
    printArray(moveArray)
    print("Start Row:", startRow, "; Start Col:", startCol)

    # curRowOne = startRow
    # curRowTwo = startRow
    # curColOne = startCol
    # curColTwo = startCol

    # sourceDirOne = "NA"
    # sourceColOne = "NA"

    moves = countMoves(moveArray, startRow, startCol, False)
    print(moves)

    moveOut = countMoves(moveArray, startRow, startCol, True)[1]

    outFile = open('TenOut.txt', 'w', encoding='UTF-8')

    for line in moveOut:
        lineString = ""
        for i in line:
            lineString += i + " "
        outFile.write(lineString + "\n")

    # Generated a map with the loop and spaces labeled, attempted to count via sheet, worked, do not have the sheet scripts included.

    outFile.close()
    dataFile.close()

    return

main()