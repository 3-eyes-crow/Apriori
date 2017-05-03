import random
import csv


def random_line():
    start = ['I' + str(x) for x in range(1, 14)]
    end = ['I13', 'I6', 'I5', 'I10', 'I11', 'I3', 'I12']
    road = {'I1': ['I2', 'I8', 'I4', 'I6'], 'I2': ['I3', 'I1', 'I12'], 'I3': ['I11', 'I2'], 'I4': ['I1', 'I9', 'I5'],
            'I5': ['I4', 'I10'],
            'I6': ['I1', 'I7'],
            'I7': ['I12', 'I6'], 'I8': ['I1', 'I9', 'I11'], 'I9': ['I4', 'I10', 'I8'], 'I10': ['I9', 'I5'],
            'I11': ['I3', 'I8'], 'I12': ['I3', 'I7'],
            'I13': ['I7']}

    line = []
    begin = start[random.randint(0, len(start) - 1)]
    line.append(begin)
    nextnode = road[begin][random.randint(0, len(road[begin]) - 1)]
    line.append(nextnode)
    step = random.randint(1, 10)
    for i in range(step):
        nextnode = road[nextnode][random.randint(0, len(road[nextnode]) - 1)]
        line.append(nextnode)
        if nextnode in end:
            break
    return line


if __name__ == '__main__':
    csvfile = open('d://random_line.csv', 'w', newline="")
    writer = csv.writer(csvfile)
    for k in range(100):
        writer.writerow(random_line())
    csvfile.close()
