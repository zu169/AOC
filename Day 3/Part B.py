def commonValue(g:list):
    value = 0
    common = set(g[0]) & set(g[1]) & set(g[3])
    char: str = common[0]
    print(char)
    if char.isupper() == True:
        value = ord(char) - 38
    elif char.islower() == True:
        value = ord(char) - 96
    #print(value)
    return value

def main():
    f = open('C:\#dev\AOC - Solutions\AdventOfCode2022\Day 3\input.txt', 'r') 
    rucksacks = [i for i in f.read().strip().split("\n")]
    groupValue: list = []
    group : list = []
    for rucksack in rucksacks:
        if len(group) < 3:
            group.append(rucksack)
        else:
            groupValue.append(commonValue(group))
            group.clear()
            group.append(rucksack)
    
    if group !=  None:
            groupValue.append(commonValue(group))
            group.clear()
    print(sum(groupValue))

main()