numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}


def sumValues(values):
    sum = 0
    for value in values:
        sum += value
    return sum


def checkForDigit(potential):
    for key, value in numbers.items():
        if key in potential:
            return value
    return potential


def findCalibrationValues(calibrationData):
    values = []
    for line in calibrationData:
        potential_forward_num = ""
        potential_backward_num = ""
        first = ""
        last = ""
        forward = 0
        backward = len(line) - 1
        print(line)
        while True:
            if line[forward].isdigit():
                first = line[forward]
            else:
                potential_forward_num += line[forward]
                potential_forward_num = checkForDigit(potential_forward_num)
                if potential_forward_num.isdigit():
                    first = potential_forward_num

            if line[backward].isdigit():
                last = line[backward]
            else:
                potential_backward_num += line[backward]
                potential_backward_num = checkForDigit(potential_backward_num[::-1])[
                    ::-1
                ]
                if potential_backward_num.isdigit():
                    last = potential_backward_num

            if first != "" and last != "":
                break

            if first == "":
                forward += 1
            if last == "":
                backward -= 1
            print(f"pf: {potential_forward_num} pb: {potential_backward_num}")
        print(f"line: {line} first: {first} last: {last}")
        values.append(int(first + last))

    return sumValues(values)


def main():
    documents = open("input.txt", "r")
    calibrationData = documents.read().splitlines()
    print(findCalibrationValues(calibrationData))


main()
