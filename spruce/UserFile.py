import sys
from enum import Enum
from typing import NamedTuple, Union

import requests

IMAGE_EXTENSIONS = ("GIF", "JPG", "PNG")


class Token(Enum):
    TITLE = 1
    AUTHOR = 2
    BODY = 3
    IMAGE = 4
    BULLET_POINT = 4


class Image:
    def __init__(self, url):
        self.url = url
        self.filename = self.url.split(",")[-1]
        if self.filename[-3:] not in IMAGE_EXTENSIONS:
            raise AttributeError(
                "The extension of the specified URL {} is not valid. URLs must end with a '.' followed by one of: "
                "{}".format(self.filename, ", ".format(map(lambda x: x.lower(), IMAGE_EXTENSIONS))))

    def download(self):
        return requests.get(self.url).content


class Title:
    def __init__(self, text, font_size=12):
        self.text = text


class ListTypes(Enum):
    BULLET = 1
    NUMBER = 2
    ROMAN_NUMBER = 3
    LETTER_UPPERCASE = 4
    LETTER_LOWERCASE = 5


class List(NamedTuple):
    list_type: ListTypes
    items: str


class Author:
    def __init__(self, name):
        self.name = name


class TokenValue(NamedTuple):
    token: Token
    value: Union[Image, Title]


def download_image(url, filename):
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)


def get():
    userFilePath = sys.argv[1]
    linesData = open(userFilePath).read().splitlines()

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

    return fileData
