import csv
import xlrd
from dateutil import parser
import datetime
import re


#Write found combinations to this file
outputFile = open('formattedNodes.csv', 'w',newline='')
writer = csv.writer(outputFile, delimiter=',', quotechar='"')

with open('unformattedNodes.csv', 'rt',encoding='latin1') as file:
    reader = csv.reader(file)
    streetWorkCombos = []
    passCount = 0
    for row in reader:
        if not (row[0] == 'n'):
            splittedVersion = row[0].split(',')
            placeholder = re.search("\[(.*?)\]", splittedVersion[1])
            label = placeholder.group(1)

            splitV2 = splittedVersion[2].split(':{')
            remadeFirstProperty = "\"Node Label\"," + label + ',' + splitV2[1].split(':')[0] + ',' + splitV2[1].split(':')[1]

            finalString = ""

            for element in range(0,len(splittedVersion)):
                print(finalString)
                if element == 0:
                    finalString = finalString + ''.join(splittedVersion[element].split(':')[1:]) + ','
                    continue
                if element == 1:
                    print(splittedVersion[element])
                    finalString = finalString
                    continue
                if element == 2:
                    finalString = finalString + (remadeFirstProperty + ',')
                    continue
                if element == len(splittedVersion)-1:
                    finalString = finalString + splittedVersion[element].split(':')[0] + ',' + ''.join(splittedVersion[element].split(':')[1:]).split('}')[0]
                    # print(finalString)
                else:
                    finalString = finalString + (splittedVersion[element].split(':')[0] + ',' + ''.join(splittedVersion[element].split(':')[1:]) + ',')

            print("hoi")
            writer.writerow([finalString])

