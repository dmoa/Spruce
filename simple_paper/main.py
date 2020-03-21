import PPTX
import UserFile

fileInfo = UserFile.get()
presentation = PPTX.get(fileInfo)

presentation.save("example/test.pptx")