import sys
import fileinput
import urllib.request

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

        # "" -> new slide
        if line == "":
            slides.append({
                "Title": linesData[i+1],
                "Body": "",
                "Image": ""
            })

        # "@" -> image url
        elif line[:2] == "@ ":
            fileName = line[2:].replace("/", "").replace(".", "").replace(":","") + ".png"
            print("Downloading Image")
            urllib.request.urlretrieve(line[2:], fileName)
            slides[-1].update( {"Image": fileName} )

        # "-" -> bullet point
        elif line[:2] == "- ":
            newBulletPoint = "-\t" + line[2:] + "\n"
            slides[-1]["Body"] += newBulletPoint

    return fileData