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


def addUpPartNumbers(schematic):
    part_number_sum = 0
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
        num = ""
        for i, val in enumerate(current_line):
            if val in num:
                continue
            else:
                num = ""
            if val.isdigit():
                num = val
                # check multi digit number
                n = i + 1
                while current_line[n].isdigit():
                    num += current_line[n]
                    if n + 1 < len(current_line):
                        n += 1
                    else:
                        break
                print(
                    f"num: {num} current index: {i} next index: {n} val: {current_line[51]}"
                )
                part_number_sum += isAdjacentSymbol(
                    num, i, previous_line, current_line, next_line
                )
                print(part_number_sum)

    return part_number_sum


def main():
    documents = open("Day3/input.txt", "r")
    schematic = documents.read().splitlines()
    print(addUpPartNumbers(schematic))


main()
