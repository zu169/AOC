wins = {"A":"Y", "B":"Z", "C":"X"}
draws = {"A":"X", "B":"Y", "C": "Z"}
losses = {"A":"Z", "B":"X", "C": "Y"}

def checkIfWin(p1,p2):
    score = 0
    #check shape score
    match p2:
        case "X":
            score += 1
        case "Y":
            score += 2
        case "Z":
            score += 3 
    #check game score
    if wins.get(p1) == p2:
        score += 6
    elif draws.get(p1) == p2:
        score += 3
    return score

def main():
    moves = open('C:\#dev\AOC - Solutions\AdventOfCode2022\Day 2\input.txt', 'r') 
    games = moves.readlines()
    totalScore = 0
    for game in games:
        totalScore += checkIfWin(game[0], game[2])
    print(totalScore)

main()