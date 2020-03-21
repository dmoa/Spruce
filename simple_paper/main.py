import PPTX
import UserFile

fileInfo = UserFile.get()
presentation = PPTX.get(fileInfo)
presentation.save("test.pptx")