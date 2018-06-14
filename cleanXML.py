import re
import xml.etree.ElementTree as ET

def readTillNextText(f):
    c=True
    text = ""
    while c:
        line = f.readline()
        if "</text>" in line:
            c=False
        else:
            text = text + " "+line
    return text

def removeTagFromText(text):
    return re.sub(r'<(.*?)>', "", text)

with open("./learners_cleaned.xml", 'w') as f2:
    with open("./learners.xml") as f:
        c = False
        while (f):
            line = f.readline()
            if "</root>" in line:
                f2.write("</root>")
                break
            if "<text>" in line:
                #                 print (line)
                text = readTillNextText(f)
                text = removeTagFromText(text)
                text = "<text>" + text + "</text>\n"
                f2.write(text)
            else:
                f2.write(line)
# print (line)



