#Day 1: Calorie Counting
def findMaxCalories(foodCalories):
    elves: list = []
    temp = 0
    #total all calories carried by each elf and store in a list
    for line in foodCalories:
        if line == '\n':
            elves.append(temp)
            temp = 0
        else: temp += int(line)
    #find the highest total calories carried by an elf
    return max(elves)

def main():
    foodCals = open('C:\#dev\AOC - Solutions\AdventOfCode2022\Day 1\input.txt', 'r') 
    data = foodCals.readlines()
    print(findMaxCalories(data))
   
main()
