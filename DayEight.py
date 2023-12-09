# Advent of Code Day 8

import re
import math

def sortNodes(list):
    nameList = []
    for name in list:
        nameList.append(name.name)

    nameList.sort()

    sortedList = [None] * len(list)

    for item in list:
        index = nameList.index(item.name)
        sortedList[index] = item
    
    return sortedList

def getStartingNodes(list):
    output = []
    for item in list:
        if item[2] == 'A':
            output.append(item)
    return output

def countMoves(nameList, nodeData, startNode, moveList):
    currentNode = startNode
    currentIndex = nameList.index(startNode)
    moves = 0
    moveIndex = 0

    while currentNode[2] != 'Z':
        move = moveList[moveIndex]
        if move == 'L':
            currentNode = nodeData[currentIndex][1]
            currentIndex = nameList.index(currentNode)
        else:
            currentNode = nodeData[currentIndex][2]
            currentIndex = nameList.index(currentNode)
        moves += 1
        moveIndex += 1
        if moveIndex == len(moveList):
            moveIndex = 0
    return moves


def main():
    dataFile = open('DayEight.txt', 'r', encoding='UTF-8')

    movePattern = dataFile.readline().strip()
    dataFile.readline()
    nodes = []

    # for line in dataFile:
    #     nodeData = re.findall('[A-Z]{1,3}', line)
    #     nodeName = nodeData[0]
    #     leftName = nodeData[1]
    #     rightName = nodeData[2]
    #     newNode = Node(nodeName, leftName, rightName)
    #     nodes.append(newNode)
    #     print(nodeData)
    
    # nodes = sortNodes(nodes)
    # for node in nodes:
    #     print(node.name)

    nodeNames = []
    nodeData = []

    for line in dataFile:
        data = re.findall('[A-Z]{1,3}', line)
        nodeNames.append(data[0])
        nodeData.append(data)

    # currentNode = "AAA"
    # currentIndex = nodeNames.index('AAA')
    moveIndex = 0
    totalMoves = 0

    # Part One
    # while currentNode != 'ZZZ':
    #     move = movePattern[moveIndex]
    #     if move == 'R':
    #         currentNode = nodeData[currentIndex][2]
    #         currentIndex = nodeNames.index(currentNode)
    #     if move == 'L':
    #         currentNode = nodeData[currentIndex][1]
    #         currentIndex = nodeNames.index(currentNode)
    #     totalMoves += 1
    #     moveIndex += 1
    #     if moveIndex == len(movePattern):
    #         moveIndex = 0

    startPositions = getStartingNodes(nodeNames)
    movesNeeded = []

    for i in startPositions:
        movesNeeded.append(countMoves(nodeNames, nodeData, i, movePattern))

    print(math.lcm(*movesNeeded))

    return

main()