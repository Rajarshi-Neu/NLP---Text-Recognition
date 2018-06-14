import xml.etree.ElementTree as ET  # to parse XML
import numpy as np     # To convert list to numpy array. Used for creating
# pandas dataframe column

import pandas as pd      # used to create csv of parsed data

print ("Started reading xml file from xmlparse library...")
tree = ET.parse("./learners_cleaned.xml"	)
print ("Done reading xml files")

root = tree.getroot()


learnerid  = []
nationality = []
grade = []
level = []
topic = []
text = []

print ("Starting parsing ...")
# iterate news items
for writings in root.findall('./writings'):
    for writing in writings:
        level.append(writing.attrib['level'])
        for item in writing:
            if item.tag=="learner":
                learnerid.append(item.attrib['id'])
                nationality.append(item.attrib['nationality'])
            if item.tag=="topic":
                topic.append(item.text)
            if item.tag=="grade":
                grade.append(item.text)
            if item.tag=="text":
                text.append(item.text)

print ("Parsing completed \n")

df = pd.DataFrame(columns = ["learnerId","nationality","grade","level","topic","text"])

df['learnerId']= np.array(learnerid)
df['nationality']=np.array(nationality)
df['grade'] = np.array(grade)
df['level'] = np.array(level)
df['topic'] = np.array(topic)
df['text'] = np.array(text)

print ("dataframe creationg completed")
df.to_csv("./parsed_xmlAsCSV.csv",index=False)
print  ("Wrote parsed csv to disk with filename : parsed_xmlAsCSV.csv")