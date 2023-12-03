def main():
    documents = open("Day2/input.txt", "r")
    game_data = documents.read().splitlines()
    print(unpackGames(game_data))


main()
