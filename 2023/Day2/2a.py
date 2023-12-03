bag_contents = {"red": 12, "green": 13, "blue": 14}


def checkIfGamePossible(cubes, id):
    possible = True
    for key, value in bag_contents.items():
        if value < cubes[key]:
            possible = False
    if possible == True:
        return id
    return 0


def unpackGames(game_data):
    sum_of_ids = 0
    for game in game_data:
        cubes = {"red": 0, "green": 0, "blue": 0}
        # split game id and game information
        game = game.split(":")
        # save game id
        game_id = game[0].split(" ")
        game_id = game_id[1]
        # only use game information
        game = game[1]
        rounds = game.split(";")
        for r in rounds:
            colours = r.split(", ")
            for c in colours:
                if c[0] == " ":
                    c = c[1::]
                values = c.split(" ")
                num = values[0]
                colour = values[1]
                for key, value in cubes.items():
                    if key == colour and value < int(num):
                        cubes[key] = int(num)
        sum_of_ids += checkIfGamePossible(cubes, int(game_id))

    return sum_of_ids


def main():
    documents = open("Day2/input.txt", "r")
    game_data = documents.read().splitlines()
    print(unpackGames(game_data))


main()
