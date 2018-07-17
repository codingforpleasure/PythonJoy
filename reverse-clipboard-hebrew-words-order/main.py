import pyperclip

corruptedData = pyperclip.paste()

with open("Output.txt", "w") as fixedTextFile:
    for line in corruptedData.splitlines():
        fixedTextFile.write(' '.join(line.split()[::-1]))
