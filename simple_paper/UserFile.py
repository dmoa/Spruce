import sys
import fileinput

def get():
    lineData = []

    presentFile = sys.argv[1]
    for line in fileinput.input(presentFile):
        lineData.append(line.splitlines()[0])

    fileData = {
        "Title": lineData[0],
        "Author": lineData[1],
        "Body_Slides": []
    }

    slides = fileData["Body_Slides"]
    # lineData.pop()
    for i in range(2, len(lineData)):
        if lineData[i] == "":
            slides.append({})
        else:
            if slides[-1] == {}:
                slides[-1].update( {"Title": lineData[i]} )
                slides[-1].update( {"Body": ""} )
            else:
                newBulletPoint = "-\t" + lineData[i][2:] + "\n"
                slides[-1]["Body"] += newBulletPoint

    return fileData