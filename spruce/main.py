import PPTX
import UserFile
import sys

# First argument is python file name, so need to check if there's less than 2, not less than 1, if we want to know if file name has been passed.
if len(sys.argv) < 2:
    print("File name not given!")
    exit()

fileInfo, fileName = UserFile.get()
presentation = PPTX.get(fileInfo)
presentation.save(fileName + ".pptx")