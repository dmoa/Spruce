import PPTX
import UserFile

fileInfo, fileName = UserFile.get()
presentation = PPTX.get(fileInfo)
presentation.save(fileName + ".pptx")