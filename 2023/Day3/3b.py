def isAdjacentSymbol(num, i, previous_line, current_line, next_line):
    if i - 1 >= 0:
        if previous_line[i - 1].isdigit() == False and previous_line[i - 1] != ".":
            print("previous")
            return int(num)
        elif current_line[i - 1].isdigit() == False and current_line[i - 1] != ".":
            print("current")
            return int(num)
        elif next_line[i - 1].isdigit() == False and next_line[i - 1] != ".":
            print("next")
            return int(num)

    for n in range(i, i + len(num)):
        if previous_line[n].isdigit() == False and previous_line[n] != ".":
            print("previous above")
            return int(num)
        elif next_line[n].isdigit() == False and next_line[n] != ".":
            print("next above")
            return int(num)

    next_index = i + len(num)
    if next_index < len(current_line):
        if (
            previous_line[next_index].isdigit() == False
            and previous_line[next_index] != "."
        ):
            print("previous next")
            return int(num)
        elif (
            current_line[next_index].isdigit() == False
            and current_line[next_index] != "."
        ):
            print("current next")
            return int(num)
        elif next_line[next_index].isdigit() == False and next_line[next_index] != ".":
            print("next next")
            return int(num)

    return 0

    def checkForDigitLength(i, line):
        num = ""
        if i > 0:
            previous_i = i - 1
            while line[previous_i].isdigit():
                num += line[previous_i]
                if previous_i - 1 >= 0:
                    previous_i -= 1
                else:
                    break
            num = num[::-1]

        num += line[i]

        if i < len(line) - 1:
            next_i = i + 1
            while line[next_i].isdigit():
                num += line[next_i]
                if next_i + 1 < len(line):
                    next_i += 1
                else:
                    break

        return num

    def checkForTwoNums(i, previous_line, current_line, next_line):
        part_numbers_found = []
        if i - 1 >= 0:
            if previous_line[i - 1].isdigit():
                part_numbers_found.append(checkForDigitLength(i - 1, previous_line))
            if current_line[i - 1].isdigit():
                part_numbers_found.append(checkForDigitLength(i - 1, current_line))
            if next_line[i - 1].isdigit():
                part_numbers_found.append(checkForDigitLength(i - 1, next_line))

    def addUpGearRatios(schematic):
        gear_ratios_sum = 0
        previous_line = []
        next_line = []
        for i in schematic[0]:
            previous_line.append(".")
            next_line.append(".")

        for i, current_line in enumerate(schematic):
            if i - 1 >= 0:
                previous_line = schematic[i - 1]
            if i + 1 < len(schematic):
                next_line = schematic[i + 1]

            for i, val in enumerate(current_line):
                if val == "*":
                    gear_ratios_sum += checkForTwoNums(
                        i, previous_line, current_line, next_line
                    )

        return gear_ratios_sum


def main():
    documents = open("Day3/test.txt", "r")
    schematic = documents.read().splitlines()
    print(addUpGearRatios(schematic))


main()
