#Day 1: Calorie Counting
def topThreeCalories(foodCalories):
    elves: list = []
    temp = 0
    #total all calories carried by each elf and store in a list
    for line in foodCalories:
        if line == '\n':
            elves.append(temp)
            temp = 0
        else: temp += int(line)
    #find the highest total calories carried by an elf three times
    sum = 0
    for i in range(0,3):
        sum += max(elves)
        elves.remove(max(elves))
    return sum

def main():
    foodCals = open('C:\#dev\AOC - Solutions\AdventOfCode2022\Day 1\input.txt', 'r') 
    data = foodCals.readlines()
    print(topThreeCalories(data))

main()