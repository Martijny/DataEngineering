import csv
import xlrd
from dateutil import parser
import datetime
import re


#Write found combinations to this file
outputFile = open('formattedEdges.csv', 'w',newline='')
writer = csv.writer(outputFile, delimiter=',', quotechar='"')

with open('EdgeExample.csv', 'rt',encoding='latin1') as file:
    reader = csv.reader(file)
    for row in reader:
        if not (row[0] == 'n' or row[0]=='p'):
            placeholder = re.search("\"relationship\":(.*?),\"end\":{", row[0])
            label = placeholder.group(1)

            splittedVersion = label.split(',')

            hoi = splittedVersion[1].split(':')

            finalString = ""

            for element in range(0,len(splittedVersion)):
                if element == 1 or element == 0 or element == 2:
                    finalString = finalString + splittedVersion[element].split(':')[1] + ','
                    continue

                #Properties need to be handed differently...
                if splittedVersion[element].startswith("\"properties"):
                    print("hm")
                    print(splittedVersion[element])
                    getInitProp = splittedVersion[element].split('{')

                    #In this case no properties are set on the edges
                    if(getInitProp[1]) == '}}':
                        finalString = finalString[:-1]
                        break
                    #Properties exist on the edges
                    else:
                        finalString = finalString + (getInitProp[1].split(':')[0] + ',' + ''.join(getInitProp[1].split(':')[1:]) + ',')
                        continue

                #Extract the node label
                if element == 3:
                    finalString = finalString + ("\"Node Label\"" + ',' + splittedVersion[element].split(':')[1] + ',')
                    continue

                #Handle final element differently
                if element == len(splittedVersion)-1:
                    # print(finalString)
                    finalString = finalString + splittedVersion[element].split(':')[0] + ',' + \
                                  ''.join(splittedVersion[element].split(':')[1:]).split('}')[0]

                #Regular procedure
                else:
                    finalString = finalString + (
                    splittedVersion[element].split(':')[0] + ',' + ''.join(splittedVersion[1].split(':')[1:]) + ',')

            writer.writerow([finalString])

