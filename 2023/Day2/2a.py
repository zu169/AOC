def main():
    documents = open("input.txt", "r")
    calibrationData = documents.read().splitlines()
    print(calibrationData)


main()
