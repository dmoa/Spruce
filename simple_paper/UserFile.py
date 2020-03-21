import sys
import fileinput

def get():

    userFilePath = sys.argv[1]
    linesData = open(userFilePath).read().splitlines()

    fileData = {
        "Title": linesData.pop(0),
        "Author": linesData.pop(0),
        "Body": []
    }

    slides = fileData["Body"]

    for i in range( len(linesData) ):
        line = linesData[i]

        if line == "":
            slides.append({})
        else:
            if slides[-1] == {}:
                slides[-1].update( {"Title": line} )
                slides[-1].update( {"Body": ""} )
            else:
                newBulletPoint = "-\t" + line[2:] + "\n"
                slides[-1]["Body"] += newBulletPoint

    return fileData