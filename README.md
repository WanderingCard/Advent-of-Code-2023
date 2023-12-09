# Advent of Code 2023
Overall Statistics:
```
Stars Earned: 18
Part Ones Finished: 9 (Last: Day 9)
Part Twos Finished: 9 (Last: Day 9)
Days Completed: 9 (Last: Day 9)
```
## Day One
> Language: Python

> Finished: 11:09 PM 12/1/2023

> Parts Finished: 1 and 2

### Problem Summary
Part One:
> File containing calibration data stored within a file (DayOne.txt) find the first and last digit in each line, combine them to get a value and sum each line's value

Part Two:
> File lines contain word values of digits (I.E One, Two, Three, etc.) include those and perform the same calculation as part one.

## Day Two
> Language: Python

> Finished: 7:19 AM 12/2/2023

> Finished Both Parts

### Problem Summary
**Part One**
> Given an input consisting of a number of games involving colored cubes pulled from a bag, determine what rounds are valid assuming that a max of 12 red, 13 green and 14 blue in the bag. Get the sum of the valid round numbers


**Part Two**
> Figure out the minimum number of red, green and blue cubes that need to be in the bag assuming ALL rounds are valid. For each round multiply the minimum number of red, green and blue cubes together to get a round total. Sum up all the round totals for the final answer.


## Day Three
> Language: Python

> Finished: 7:40 AM 12/3/2023

> Finished Both Parts

### Problem Summary
**Part One**
> Given an input consisting of numbers and symbols, find the missing part numbers. Missing part numbers are numbers adjacent to some symbol (not including .). Find the sum of the missing part numbers.

**Part Two**
> Given the same input, find missing gears and their ratios. A gear is defined as any * symbol with exactly 2 values adjacent to it. The ratio is those numbers multiplied together. Sum up the ratios to get the final answer

## Day Four
> Language: Python

> Finished: 6:36 AM 12/4/2023

> Finished Both Parts

### Problem Summary
**Part One**
> Given a set of inputs representing scratchoff cards, with a set of winning numbers and card numbers, figure out the total points won amongst the entire stack of cards. Each match of a card number with a winning number (regardless of points) counts towards the points total for the card, which is 2^matches-1

**Part Two**
> For each match in the data set, you get a duplicate of a subsequent card, I.E 3 matches results in a duplicate of the next three cards being added to the pile, each copy and original of the card generates the duplicates. Figure out the total number of cards that will be played when all copies and originals are finished. 

# Day Five
> Language: Python

> Finished: 2:00 PM 12/5/2023

> Finished Both Parts

### Problem Summary
**Part One**
> You are given an input containing data on a list of seeds and various conversion rates, using this data convert the seeds through the various tables into a location value, find the lowest location value

**Part Two**
> Now the seed values are pairs representing ranges of seeds, find the lowest value out of the initial seeds.

# Day Six
> Language: Python

> Finished: 10:00 PM 12/6/2023

> Finished Both Parts

## Problem Summary

**Part One**
> You have a toy boat, who's speed over the time it runs is based on how long you hold the launch button. Given an input list of record times and a input list of race distances, figure out how many different hold times you can use to break the record for each race, and multiply those answers together for the final answer

> Instead of multiple races the time and distance inputs are for one race, figure out how many different ways the race can be won.

# Day Seven
> Language: Python

> Finished: 7:54 AM 12/7/2023

> Finsihed Both Parts

## Problem Summary

**Part One**
> Playing a game of Camel Cards! The input consists of a 5-card hand (T representing Ten) and a bid, for each hand figure out 1 what type of hand it is (Five of a Kind, Four of a Kind, Full House, Three of a Kind, Two Pairs, Pair, High) and what rank it is based on the value of the cards starting at the first and going on (Aces High) for each card its score is equal to its rank * bid, sum up the bids for the result

**Part Two**
> This time Js are not Jacks but Jokers, Jokers are wild, but for the purpose of sorting, they do not count as the card they are pretending to be (I.E AAJAA is four of a kind but the Joker is still a Joker not an Ace). Jokers are also ranked lower than twos for the purposes of balance, find the new total score from your hands

## Day Eight

> Language: Python

> Finished 10:18 PM 12/8/2023

> Finished Both Parts

### Problem Summary

**Part One**
> Given a list of nodes and nodes they are connected to, one on the right, another on the left, along with a pattern of left and right moves, determine how many moves are needed to get from node AAA to node BBB

**Part Two**
> Same Challenge as above, but now you are considering multiple starting nodes (any ending in A) and multiple ending nodes(B) and figure out how many moves it takes so that you end up on all ending nodes from an original starting node at the same time.

## Day Nine
> Language: Python

> Finished: 6:58 AM 12/9/2023

> Finished Both Parts

### Problem Summary

**Part One**
> Each line of the input data represents historical data for an oasis, predict the next value of the data. Calculate the differences between each of the data points in the line, then calculate the differences between those differences and so on until you get to a line of differences of only 0s, then work backwards and predict the next value, sum all predicted values

**Part Two**
> Same as above, except you are predicting values in the past, same method of getting the differences
