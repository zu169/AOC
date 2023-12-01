def sumValues(values):
    sum = 0
    for value in values:
        sum += int(value)
    return sum


def findCalibrationValues(calibrationData):
    digits = ""
    values = []
    for line in calibrationData:
        for value in line:
            if value.isdigit():
                digits += value
        values.append(digits[0] + digits[-1])
        digits = ""
    return sumValues(values)


def main():
    documents = open("input.txt", "r")
    calibrationData = documents.read().splitlines()
    print(calibrationData)


main()
