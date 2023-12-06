import re


def waysToBeatRecord(time, distance):
    way_to_beat_record = 0
    for i in range(1, time):
        speed = i
        time_left = time - i
        if time_left * speed > distance:
            way_to_beat_record += 1
    return way_to_beat_record


def main():
    races = open("Day6/input.txt", "r")
    raceInfo = races.read().splitlines()
    time = re.findall(r"\d+", raceInfo[0])
    distance = re.findall(r"\d+", raceInfo[1])
    beatsrecord = 1
    for i in range(0, len(distance)):
        beatsrecord *= waysToBeatRecord(int(time[i]), int(distance[i]))
    print(beatsrecord)


main()
