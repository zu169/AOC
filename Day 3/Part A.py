def findCommon(pocket1: str, pocket2: str):
    common = set(pocket1).intersection(pocket2)
    char: str = common.pop()
    if char.isupper() == True:
        value = ord(char) - 38
    elif char.islower() == True:
        value = ord(char) - 96
    return value

def main():
    f = open('C:\#dev\AOC - Solutions\AdventOfCode2022\Day 3\input.txt', 'r') 
    rucksacks = f.readlines()
    valueSum = 0
    for rucksack in rucksacks:
        pocket1, pocket2 = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
        valueSum += findCommon(pocket1, pocket2)
    print(valueSum)

main()