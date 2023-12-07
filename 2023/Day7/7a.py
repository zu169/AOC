def main():
    cards = open("Day7/test.txt", "r")
    cardData = cards.read().splitlines()
    hands = {}
    for line in cardData:
        line = line.split(" ")
        print(line)
        hands[line[0]] = line[1]

    print(hands)


main()
