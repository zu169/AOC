def getNewSequence(report):
    sequence = []
    previous = report[0]
    for num in range(1, len(report)):
        sequence.append(int(report[num]) - int(previous))
        previous = report[num]
    return sequence


def main():
    dataset = open("Day9/test.txt", "r")
    data = dataset.read().splitlines()
    total = 0
    for report in data:
        sequences = []
        newindex = 0
        sequences.append(report.split())
        while True:
            sequence = getNewSequence(sequences[newindex])
            sequences.append(sequence)
            newindex += 1
            if sum(sequence) == 0:
                break
        sequences[-1].append(0)
        next = 0
        for i in range(len(sequences) - 2, -1, -1):
            next += int(sequences[i][-1])
            sequences[i].append(next)
        total += sequences[0][-1]
    print(total)


main()
