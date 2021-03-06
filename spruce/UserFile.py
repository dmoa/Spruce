import sys
import requests

def download_image(url, filename):
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)

def remove_comments(lines):
    for i in range(len(lines)):
        if lines[i] != "" and lines[i][0] == "#":
            lines.pop(i)
            remove_comments(lines)
            break

def get():
    userFilePath = sys.argv[1]
    linesData = open(userFilePath).read().splitlines()
    remove_comments(linesData)

    print(linesData)

    fileData = {
        "Title": linesData.pop(0),
        "Author": linesData.pop(0),
        "Body": []
    }

    slides = fileData["Body"]

    for i in range(len(linesData)):
        line = linesData[i]

        # "" -> new slide
        if line == "":
            slides.append({
                "Title": linesData[i + 1],
                "Body": "",
                "Image": ""
            })

        # "@" -> image url
        elif line[:2] == "@ ":
            fileName = line[2:].replace("/", "").replace(".", "")
            fileName = fileName.replace(":", "") + ".png"
            download_image(line[2:], fileName)
            slides[-1].update({"Image": fileName})

        # "-" -> bullet point
        elif line[:2] == "- ":
            newBulletPoint = "-\t" + line[2:] + "\n"
            slides[-1]["Body"] += newBulletPoint

    return fileData, userFilePath
