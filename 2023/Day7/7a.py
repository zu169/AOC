def main():
    cards = open("Day7/test.txt", "r")
    cardData = cards.read().splitlines()
    ranks = len(cardData)
    card_types = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    ranking = {}
    hands = {}
    for line in cardData:
        line = line.split(" ")
        hands[line[0]] = line[1]
        # rate hand
        matching = {}
        for card in line[0]:
            if card in matching:
                matching[card] += 1
            else:
                matching[card] = 1
        total_matches = list(matching.values())
        for matches in total_matches:
            assignRank()

    print(hands)


main()
