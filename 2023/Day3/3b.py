def main():
    documents = open("Day3/input.txt", "r")
    schematic = documents.read().splitlines()
    gear_total = 0
    for r, row in enumerate(schematic):
        for c, ch in enumerate(row):
            if ch != "*":
                continue
            number_coordinates = set()
            # search for two nums
            for num_row in [r - 1, r, r + 1]:
                for num_col in [c - 1, c, c + 1]:
                    if (
                        num_row >= 0
                        and num_row < len(schematic)
                        and num_col >= 0
                        and num_col < len(schematic[0])
                        and schematic[num_row][num_col].isdigit()
                    ):
                        while num_col > 0 and schematic[num_row][num_col - 1].isdigit():
                            num_col -= 1
                        number_coordinates.add((num_row, num_col))
            if len(number_coordinates) != 2:
                continue
            gear_ratio = []
            for num_row, num_col in number_coordinates:
                num = ""
                while (
                    num_col < len(schematic[num_row])
                    and schematic[num_row][num_col].isdigit()
                ):
                    num += schematic[num_row][num_col]
                    num_col += 1
                gear_ratio.append(int(num))

            gear_total += gear_ratio[0] * gear_ratio[1]

    print(gear_total)


main()
