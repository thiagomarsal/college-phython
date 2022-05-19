# IT 280 – Lab #9: File Modification Instructions
from os import path
lineFormat = "{0:2d}. {1} Sample\n"


def readFile():
    lines = []
    if path.exists('./randomValues_1.txt'):
        with open('./randomValues_1.txt') as file:
            lines = file.read().splitlines()
        file.close()
    return lines


def createFile(lines):
    file = open("./randomValues_2.txt", "w+")
    file.writelines(lines)
    file.close()


def main():
    lines = readFile()
    for i in range(len(lines)):
        lines[i] = lineFormat.format(i, lines[i])
    createFile(lines)


main()
