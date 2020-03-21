import sys
import fileinput

def get():
    lineData = []

    presentFile = sys.argv[1]
    for line in fileinput.input(presentFile):
        lineData.append(line.splitlines()[0])

    fileData = {
        "Title": lineData[0],
        "Author": lineData[1]
    }

    return fileData