def getScore(p1,p2):
    score = 0
    match p1:
        #rock
        case "A":
            match p2:
                #lose = scissors
                case "X": score += 3
                #draw = rock
                case "Y":
                    score += 4
                #win = paper
                case "Z":
                    score += 8
        #paper
        case "B":
            match p2:
                #lose = rock
                case "X":
                    score += 1
                #draw = paper
                case "Y":
                    score += 5
                #win = scissors
                case "Z":
                    score += 9
        #scissors
        case "C":
            match p2:
                #lose = paper
                case "X":
                    score += 2
                #draw = scissors
                case "Y":
                    score += 6
                #win = rock
                case "Z":
                    score += 7
    return score


def main():
    moves = open('C:\#dev\AOC - Solutions\AdventOfCode2022\Day 2\input.txt', 'r') 
    games = moves.readlines()
    totalScore = 0
    for game in games:
        totalScore += getScore(game[0], game[2])
    print(totalScore)

main()