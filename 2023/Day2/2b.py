def unpackGames(game_data):
    sum_of_sets = 0
    for game in game_data:
        cubes = {"red": 0, "green": 0, "blue": 0}
        print(game)
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
        set_sum = 1
        for key, value in cubes.items():
            set_sum *= value
        sum_of_sets += set_sum

    return sum_of_sets


def main():
    documents = open("Day2/input.txt", "r")
    game_data = documents.read().splitlines()
    print(unpackGames(game_data))


main()
