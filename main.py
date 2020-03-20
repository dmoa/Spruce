import fileinput

print("Give directory of presentFile")

presentFile = input()

for line in fileinput.input(presentFile):
    print(str(line), end ="")